const fs = require('fs');
const path = require('path');

const posts = JSON.parse(fs.readFileSync(path.join(__dirname, 'posts.json'), 'utf8'));
const template = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8');

// Build directory ensure karein
const distDir = path.join(__dirname, 'dist');
if (!fs.existsSync(distDir)) {
    fs.mkdirSync(distDir, { recursive: true });
}

// Main index.html copy karein fallback ke liye
fs.copyFileSync(path.join(__dirname, 'template.html'), path.join(distDir, 'index.html'));

// Har post ke liye static folder aur index.html create karein (/post/p1, /post/p2)
posts.forEach(post => {
    const postFolder = path.join(distDir, 'post', post.id);
    fs.mkdirSync(postFolder, { recursive: true });

    let postHtml = template
        .replace(/{{TITLE}}/g, post.title)
        .replace(/{{DESC}}/g, post.desc)
        .replace(/{{POST_ID}}/g, post.id);

    fs.writeFileSync(path.join(postFolder, 'index.html'), postHtml);
    console.log(`Generated static SEO folder: /post/${post.id}/index.html`);
});

console.log('✅ SEO Pre-rendering Build Completed Successfully!');