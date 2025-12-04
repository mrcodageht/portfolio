landing_page = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio CMS - Gérez votre portfolio facilement</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #1e293b;
            --accent: #10b981;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            overflow-x: hidden;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary) 0%, #1d4ed8 100%);
            color: white;
            min-height: 100vh;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: moveGrid 20s linear infinite;
        }

        @keyframes moveGrid {
            0% { transform: translate(0, 0); }
            100% { transform: translate(50px, 50px); }
        }

        .navbar {
            padding: 20px 0;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            transition: all 0.3s ease;
        }

        .navbar.scrolled {
            background: rgba(30, 41, 59, 0.95) !important;
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .navbar-brand {
            font-size: 24px;
            font-weight: bold;
            color: white !important;
        }

        .nav-link {
            color: rgba(255,255,255,0.9) !important;
            margin: 0 15px;
            transition: all 0.3s;
        }

        .nav-link:hover {
            color: white !important;
            transform: translateY(-2px);
        }

        .hero-content {
            position: relative;
            z-index: 5;
            padding: 150px 0 100px 0;
        }

        .hero h1 {
            font-size: 56px;
            font-weight: 800;
            margin-bottom: 20px;
            animation: fadeInUp 1s ease;
        }

        .hero p {
            font-size: 22px;
            opacity: 0.95;
            margin-bottom: 40px;
            animation: fadeInUp 1s ease 0.2s backwards;
        }

        .btn-hero {
            padding: 15px 40px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
            animation: fadeInUp 1s ease 0.4s backwards;
        }

        .btn-primary-hero {
            background: white;
            color: var(--primary);
        }

        .btn-primary-hero:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .btn-outline-hero {
            background: transparent;
            color: white;
            border: 2px solid white;
            margin-left: 15px;
        }

        .btn-outline-hero:hover {
            background: white;
            color: var(--primary);
            transform: translateY(-3px);
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-image {
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        /* Features Section */
        .features {
            padding: 100px 0;
            background: #f8fafc;
        }

        .section-title {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .section-subtitle {
            font-size: 18px;
            color: #64748b;
            margin-bottom: 60px;
        }

        .feature-card {
            background: white;
            padding: 40px 30px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.07);
            transition: all 0.3s;
            height: 100%;
            border: 2px solid transparent;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.12);
            border-color: var(--primary);
        }

        .feature-icon {
            width: 70px;
            height: 70px;
            background: linear-gradient(135deg, var(--primary), #1d4ed8);
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 25px;
            font-size: 32px;
            color: white;
        }

        .feature-card h3 {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 15px;
            color: var(--secondary);
        }

        .feature-card p {
            color: #64748b;
            line-height: 1.7;
        }

        /* Tech Stack Section */
        .tech-stack {
            padding: 100px 0;
            background: white;
        }

        .tech-badge {
            display: inline-flex;
            align-items: center;
            padding: 15px 30px;
            background: #f1f5f9;
            border-radius: 50px;
            margin: 10px;
            font-weight: 600;
            color: var(--secondary);
            transition: all 0.3s;
        }

        .tech-badge:hover {
            background: var(--primary);
            color: white;
            transform: scale(1.1);
        }

        .tech-badge i {
            margin-right: 10px;
            font-size: 24px;
        }

        /* CTA Section */
        .cta {
            padding: 100px 0;
            background: linear-gradient(135deg, var(--secondary) 0%, #0f172a 100%);
            color: white;
            position: relative;
            overflow: hidden;
        }

        .cta::before {
            content: '';
            position: absolute;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(37,99,235,0.3), transparent);
            border-radius: 50%;
            top: -200px;
            right: -200px;
        }

        .cta h2 {
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 20px;
        }

        .cta p {
            font-size: 20px;
            opacity: 0.9;
            margin-bottom: 40px;
        }

        /* Footer */
        footer {
            background: var(--secondary);
            color: white;
            padding: 40px 0;
            text-align: center;
        }

        footer a {
            color: var(--primary);
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 36px;
            }

            .hero p {
                font-size: 18px;
            }

            .btn-outline-hero {
                margin-left: 0;
                margin-top: 10px;
            }

            .section-title {
                font-size: 32px;
            }
        }
    </style>
</head>
<body>
    <!-- Hero Section -->
    <section class="hero">
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg">
            <div class="container">
                <a class="navbar-brand" href="#">
                    <i class="fas fa-briefcase"></i> Portfolio CMS
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" style="background: white;">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#features">Fonctionnalités</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#tech">Technologies</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#cta">Commencer</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container hero-content">
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <h1>Gérez votre portfolio en toute simplicité</h1>
                    <p>Un système de gestion de contenu moderne et intuitif pour organiser vos projets, technologies et collaborateurs.</p>
                    <button class="btn btn-primary-hero">
                        <i class="fas fa-rocket"></i> Commencer maintenant
                    </button>
                    <button class="btn btn-outline-hero">
                        <i class="fas fa-play-circle"></i> Voir la démo
                    </button>
                </div>
                <div class="col-lg-6 text-center hero-image">
                    <i class="fas fa-laptop-code" style="font-size: 300px; opacity: 0.2;"></i>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
        <div class="container">
            <div class="text-center">
                <h2 class="section-title">Fonctionnalités puissantes</h2>
                <p class="section-subtitle">Tout ce dont vous avez besoin pour gérer votre portfolio professionnel</p>
            </div>
            
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-project-diagram"></i>
                        </div>
                        <h3>Gestion de projets</h3>
                        <p>Ajoutez, modifiez et organisez vos projets avec une interface intuitive. Associez technologies et collaborateurs facilement.</p>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-code"></i>
                        </div>
                        <h3>Catalogue de technologies</h3>
                        <p>Maintenez à jour vos compétences techniques avec un système de catégorisation et de niveaux de maîtrise.</p>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-users"></i>
                        </div>
                        <h3>Réseau de collaborateurs</h3>
                        <p>Gardez une trace de tous vos collaborateurs et partenaires avec leurs informations de contact.</p>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <h3>Dashboard analytique</h3>
                        <p>Visualisez vos statistiques en temps réel et suivez l'évolution de votre portfolio.</p>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <h3>Responsive Design</h3>
                        <p>Interface optimisée pour tous les appareils - desktop, tablette et mobile.</p>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="feature-icon">
                            <i class="fas fa-bolt"></i>
                        </div>
                        <h3>Performant et rapide</h3>
                        <p>Construit avec les meilleures pratiques pour une expérience utilisateur fluide et réactive.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Tech Stack Section -->
    <section id="tech" class="tech-stack">
        <div class="container">
            <div class="text-center">
                <h2 class="section-title">Technologies utilisées</h2>
                <p class="section-subtitle">Un stack simple et efficace</p>
            </div>
            
            <div class="text-center">
                <span class="tech-badge">
                    <i class="fab fa-html5"></i> HTML5
                </span>
                <span class="tech-badge">
                    <i class="fab fa-css3-alt"></i> CSS3
                </span>
                <span class="tech-badge">
                    <i class="fab fa-bootstrap"></i> Bootstrap 5
                </span>
                <span class="tech-badge">
                    <i class="fab fa-js"></i> JavaScript
                </span>
                <span class="tech-badge">
                    <i class="fas fa-font-awesome"></i> Font Awesome
                </span>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="cta" class="cta">
        <div class="container text-center" style="position: relative; z-index: 5;">
            <h2>Prêt à transformer votre portfolio ?</h2>
            <p>Commencez à organiser vos projets dès aujourd'hui avec Portfolio CMS</p>
            <button class="btn btn-primary-hero">
                <i class="fas fa-arrow-right"></i> Accéder au CMS
            </button>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2025 Portfolio CMS. Créé avec <i class="fas fa-heart" style="color: #e74c3c;"></i> pour les développeurs.</p>
            <p>
                <a href="#"><i class="fab fa-github"></i> GitHub</a> • 
                <a href="#"><i class="fab fa-twitter"></i> Twitter</a> • 
                <a href="#"><i class="fab fa-linkedin"></i> LinkedIn</a>
            </p>
        </div>
    </footer>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/js/bootstrap.bundle.min.js"></script>
    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Navbar background on scroll
        window.addEventListener('scroll', () => {
            const navbar = document.querySelector('.navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Animate on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.feature-card').forEach((card) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.transition = 'all 0.6s ease';
            observer.observe(card);
        });
    </script>
</body>
</html>
"""