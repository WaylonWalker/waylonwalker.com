## 50

- working custom og pages

## 49

- upgrade from markata 0.9.1.dev6 to markata 0.9.1.dev7
- 47 was missing og properties

## 48

- upgrade from markata 0.9.1.dev5 to markata 0.9.1.dev6
- fix old feed slugs with broken links with redirect
- fix drafts not populating
- add word break for long admonition titles

## 47

- upgrade from tailwind v 3.3.5 to tailwind v4.0.4
- upgrade from markata 0.9.1.dev3 to markata 0.9.1.dev5
- mermaid plugin support for ``` mermaid with a space between the fence and name

## 46

version 46 comes with many new features for markdown posts.

### more-cinematic

Adding a more-cinematic tag makes the image full width.

#### Before

``` markdown
![screenshot-2025-02-03T02-13-38-628Z.png](https://dropper.wayl.one/api/file/2f706c5d-c591-4465-8d2b-eb18ce26aeca.png){.more-cinematic}
```

![image](https://dropper.wayl.one/api/file/1f656349-d8fb-44a3-8ab3-7a4ce72414d7.webp)

#### After

![image](https://dropper.wayl.one/api/file/a55d35e5-6d8e-4379-a241-b6ab9c3c0ed3.webp)

### vsplit

Adding a vsplit tag makes the content split into two columns.

``` markdown
!!! vsplit I Have two opinions

    !!! vsplit Left Opinion

        supporting arguments

        * lorem ipsum
        * ipsum dolor

        - [x] lorem ipsum
        - [ ] ipsum dolor

    !!! vsplit Right Opinion

        supporting arguments

        * lorem ipsum
        * ipsum dolor

        - [ ] lorem ipsum
        - [x] ipsum dolor

```

![image](https://dropper.wayl.one/api/file/d5caebcc-573a-45cf-b0c8-cb758799a3d1.webp)

### mermaid

Added mermaid block support.

![image](https://dropper.wayl.one/api/file/167a1872-788f-4a85-9d25-6b81a8a31de5.webp)

![image](https://dropper.wayl.one/api/file/90c7c02e-e03c-4521-9c39-b99369f789b4.webp)
