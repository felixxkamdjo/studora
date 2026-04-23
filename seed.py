import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import User
from projects.models import Project
from applications.models import Application


def run():
    print('Nettoyage des données existantes...')
    Application.objects.all().delete()
    Project.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()

    print('Création des utilisateurs...')

    teacher1 = User.objects.create_user(
        username='teacher@univ.cm',
        email='teacher@univ.cm',
        password='password123',
        first_name='Jean',
        last_name='Dupont',
        role='teacher',
    )

    teacher2 = User.objects.create_user(
        username='teacher2@univ.cm',
        email='teacher2@univ.cm',
        password='password123',
        first_name='Marie',
        last_name='Mbarga',
        role='teacher',
    )

    student1 = User.objects.create_user(
        username='student@univ.cm',
        email='student@univ.cm',
        password='password123',
        first_name='Paul',
        last_name='Nkono',
        role='student',
    )

    student2 = User.objects.create_user(
        username='student2@univ.cm',
        email='student2@univ.cm',
        password='password123',
        first_name='Ines',
        last_name='Talla',
        role='student',
    )

    student3 = User.objects.create_user(
        username='student3@univ.cm',
        email='student3@univ.cm',
        password='password123',
        first_name='Boris',
        last_name='Kamga',
        role='student',
    )

    print('Création des projets...')

    p1 = Project.objects.create(
        title='Développement d\'une application de gestion scolaire',
        description='Ce projet vise à développer une application web complète pour la gestion des notes, absences et emplois du temps des étudiants de l\'université.',
        domain='informatique',
        teacher=teacher1,
        max_students=2,
        status='open',
    )

    p2 = Project.objects.create(
        title='Analyse des données climatiques du Cameroun',
        description='Étude et modélisation des données météorologiques collectées sur 10 ans dans les principales villes camerounaises à l\'aide de méthodes statistiques avancées.',
        domain='mathematiques',
        teacher=teacher1,
        max_students=1,
        status='open',
    )

    p3 = Project.objects.create(
        title='Plateforme e-learning pour les lycées',
        description='Conception et développement d\'une plateforme d\'apprentissage en ligne adaptée aux besoins des lycéens camerounais avec support hors-ligne.',
        domain='informatique',
        teacher=teacher2,
        max_students=3,
        status='open',
    )

    p4 = Project.objects.create(
        title='Étude de l\'impact des énergies renouvelables',
        description='Analyse technico-économique de l\'intégration des énergies solaire et hydraulique dans le réseau électrique national.',
        domain='physique',
        teacher=teacher2,
        max_students=2,
        status='closed',
    )

    print('Création des candidatures...')

    Application.objects.create(
        student=student1,
        project=p1,
        motivation='Je suis passionné par le développement web et j\'ai déjà réalisé plusieurs projets similaires durant ma formation. Je maîtrise Python, Django et React.',
        status='pending',
    )

    Application.objects.create(
        student=student2,
        project=p1,
        motivation='Ce projet correspond parfaitement à mon profil. J\'ai une solide expérience en bases de données et en conception d\'interfaces utilisateur.',
        status='accepted',
    )

    Application.objects.create(
        student=student3,
        project=p2,
        motivation='Les mathématiques appliquées et l\'analyse de données sont mes domaines de prédilection. J\'ai travaillé avec R et Python pour des analyses statistiques.',
        status='pending',
    )

    Application.objects.create(
        student=student1,
        project=p3,
        motivation='Je souhaite contribuer à l\'amélioration de l\'éducation au Cameroun. Je connais les technologies web modernes et j\'ai de l\'expérience en UX design.',
        status='rejected',
    )

    print('\nDonnées de test créées avec succès !\n')
    print('Comptes disponibles :')
    print('  Enseignant 1 : teacher@univ.cm  / password123')
    print('  Enseignant 2 : teacher2@univ.cm / password123')
    print('  Étudiant 1   : student@univ.cm  / password123')
    print('  Étudiant 2   : student2@univ.cm / password123')
    print('  Étudiant 3   : student3@univ.cm / password123')


if __name__ == '__main__':
    run()