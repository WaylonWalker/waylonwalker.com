module.exports = async (tp) => {
    const title = await tp.system.prompt("Post title");
    function slugify(s) {
        return s.normalize("NFKD").replace(/[\u0300-\u036f]/g, "")
            .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
    }
    const slug = slugify(title);
    const filePath = `pages/blog/${slug}.md`;
    await tp.file.create_new(tp.file.find_tfile("Blog Post.md"), filePath);
};
