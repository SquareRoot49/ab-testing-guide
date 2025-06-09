// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// 导航栏激活状态
window.addEventListener('scroll', function() {
    let sections = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('.nav-link');
    
    sections.forEach(section => {
        let top = section.offsetTop - 100;
        let bottom = top + section.offsetHeight;
        let scroll = window.scrollY;
        let id = section.getAttribute('id');
        
        if (scroll >= top && scroll < bottom) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + id) {
                    link.classList.add('active');
                }
            });
        }
    });
});

// 代码块复制功能
document.querySelectorAll('pre code').forEach((block) => {
    const button = document.createElement('button');
    button.className = 'copy-button';
    button.textContent = 'Copy Code';
    
    block.parentNode.style.position = 'relative';
    block.parentNode.appendChild(button);
    
    button.addEventListener('click', async () => {
        try {
            await navigator.clipboard.writeText(block.textContent);
            button.textContent = 'Copied!';
            setTimeout(() => {
                button.textContent = 'Copy Code';
            }, 2000);
        } catch (err) {
            console.error('Failed to copy:', err);
            button.textContent = 'Copy Failed';
        }
    });
});

// 添加代码块样式
const style = document.createElement('style');
style.textContent = `
    .copy-button {
        position: absolute;
        top: 5px;
        right: 5px;
        padding: 5px 10px;
        background: #e9ecef;
        border: none;
        border-radius: 3px;
        cursor: pointer;
        font-size: 12px;
        transition: background 0.3s;
    }
    
    .copy-button:hover {
        background: #dee2e6;
    }
`;
document.head.appendChild(style);

// 添加页面加载动画
document.addEventListener('DOMContentLoaded', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s';
        document.body.style.opacity = '1';
    }, 100);
}); 