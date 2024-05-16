document.addEventListener('DOMContentLoaded', (event) => {
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
          e.preventDefault();

          document.querySelector(this.getAttribute('href')).scrollIntoView({
              behavior: 'smooth'
          });
      });
  });

  // Toggle mobile navigation menu
  const nav = document.querySelector('nav ul');
  const menuToggle = document.createElement('button');
  menuToggle.classList.add('menu-toggle');
  menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
  document.querySelector('header .header-inner').prepend(menuToggle);

  menuToggle.addEventListener('click', () => {
      nav.classList.toggle('show-menu');
  });

  // Close mobile menu when link is clicked
  nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
          if (nav.classList.contains('show-menu')) {
              nav.classList.remove('show-menu');
          }
      });
  });
});
