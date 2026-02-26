---
date: 2026-02-26 09:59:57
templateKey: blog-post
title: Vaulted Secrets Without Git Churn
tags:
  - bash
  - ansible
published: False
authors:
  - waylon
  - id: gpt-5.2-codex
    role: drafter
    details: Initial draft prepared by the assistant.

---


Ansible Vault keeps secrets out of sight, but the ciphertext changes on every
encrypt. That turns Git diffs into noise and makes it hard to tell if anything
actually changed. Decrypting, editing, and re-encrypting often leaves
uncertainty about whether any plaintext changed. This is amplified when secret
repos are tightly coupled to dependent repositories. A typical cycle includes
decrypting, adding a key, updating a value, applying changes, and returning
later with little clarity about what changed while secrets were in plaintext.

Today a new workflow was created with @gpt-5.2-codex to keep diffs clean and
avoid re-encrypting when the plaintext is identical.

!!! chat-reply

    This repo has ansible vaulted secrets and an encrypt/decrypt process, but no
    way to compare. Please research compare options. The goal is to avoid
    changing files on encrypt/decrypt when plaintext is unchanged, ideally by
    comparing decrypted content and reusing the remote encrypted file.

!!! chat @gpt-5.2-codex

    The repo workflow will be reviewed, compare options identified, and a
    low-churn GitOps approach proposed to avoid re-encrypt noise.

## The problem

Re-encrypting a file with the same content produces different ciphertext. A
simple decrypt/encrypt cycle can look like a full file change, even when the
plaintext is identical. That creates uncertainty and makes GitOps workflows feel
brittle.

!!! chat-reply

    Minimal changes needed to keep GitOps clear?

!!! chat @gpt-5.2-codex

    Add compare-before-encrypt, decrypted diffs, and ignore cache artifacts.

## The solution at a glance

Three pieces make it work:

1. **Compare-before-encrypt**

    - `just decrypt` stores a plaintext hash and caches the current encrypted
      file.
    - `just encrypt` compares the plaintext hash and, if unchanged, restores the
      cached ciphertext instead of re-encrypting.

1. **Readable diffs for vaulted files**

    - `.gitattributes` sets `private/* diff=ansible-vault`.
    - A small `textconv` script decrypts for `git diff`.

1. **Ignored cache artifacts**

    - `.vault-hashes/` and `.vault-cache/` are ignored so they never hit the
      repo.

## How it works

!!! chat-reply

    How does compare-before-encrypt operate?

!!! chat @gpt-5.2-codex

    Hash plaintext on decrypt, reuse cached ciphertext on encrypt if the hash matches.

### Compare-before-encrypt

When a file is decrypted, a SHA-256 hash of the plaintext is created and stored
in `.vault-hashes/`. A copy of the encrypted file is stored in `.vault-cache/`.

When encrypting, the current plaintext file is hashed. If the hash matches the
cached hash, the cached encrypted file is restored instead of generating new
ciphertext. Result: no churn when nothing actually changed.

### Decrypted diffs

Git is configured to use `ansible-vault view` as a text conversion step for
files under `private/`. As a result, `git diff` shows decrypted content instead
of ciphertext.

Enable the diff driver locally:

```bash
git config diff.ansible-vault.textconv "scripts/ansible-vault-diff"
```

## What changes will be seen

- If a secret changes: the diff shows the plaintext change.
- If decrypt and re-encrypt occurs without changes: the diff stays clean.
- Large base64 blobs may still look like full-line diffs because they are
  single-line values.

!!! chat-reply
    What is the day-to-day workflow?

!!! chat @gpt-5.2-codex
    `just decrypt`, edit, then `just encrypt`. Clean diffs, no churn.

## Recommended usage

```bash
just decrypt
# apply edits
just encrypt
```

That is sufficient to keep Git history clean and reduce uncertainty about
whether a secret actually changed.

