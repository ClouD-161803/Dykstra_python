# Dykstra Project

Project investigating Dykstra's algorithm for Hilbert space projection onto convex sets' intersection.

## STRUCTURE:
echo "
|   README.md
|   structure.txt
|   
+---.idea
|   |   .gitignore
|   |   Dykstra.iml
|   |   misc.xml
|   |   modules.xml
|   |   vcs.xml
|   |   workspace.xml
|   |   
|   \---inspectionProfiles
|           profiles_settings.xml
|           Project_Default.xml
|           
+---Application
|   |   A Convergence Analysis of Dykstra's Algorithm for Polyhedral Sets.pdf
|   |   EUROP Sample Application.docx
|   |   EUROP Sample Application.pdf
|   |   EUROP Student Guidance 2023-24.pdf
|   |   Fast Gradient Method.pdf
|   |   Model_Predictive_Control_for_Electron_Beam_Stabilization_in_a_Synchrotron.pdf
|   |   On Dykstra’s algorithm_ finite convergence, stalling, and the method of alternating projections journal.pdf
|   |   slides_claudio.pdf
|   |   Student_sheets.pdf
|   |   
|   \---Final Drafts
|           EUROP Application - Claudio Vestini.docx
|           EUROP Application - Claudio Vestini.pdf
|           Modified EUROP Application - Claudio Vestini.docx
|           
+---Books & Articles
|   |   A Convergence Analysis of Dykstra's Algorithm for Polyhedral Sets.pdf
|   |   Advanced_Textbooks_in_Control_and_Signal.pdf
|   |   Fast Gradient Method.pdf
|   |   Model_Predictive_Control_for_Electron_Beam_Stabilization_in_a_Synchrotron.pdf
|   |   On Dykstra’s algorithm_ finite convergence, stalling, and the method of alternating projections journal.pdf
|   |   
|   +---Baushke
|   |   |   arXiv-2001.06747v1.tar.gz
|   |   |   
|   |   \---arXiv-2001.06747v1
|   |           arxiv.tex
|   |           DifferentSequences.png
|   |           StallingRegionsHand.png
|   |           
|   +---claudio_projection
|   |       On Dykstra’s algorithm_ finite convergence, stalling, and the method of alternating projections journal.pdf
|   |       On Dykstra’s algorithm_ finite convergence, stalling, and the method of alternating projections.pdf
|   |       Projection Methods_ Swiss Army Knives for Solving Feasibility and Best Approximation Problems with Halfspaces.pdf
|   |       Proximal Splitting Methods in Signal Processing.pdf
|   |       The rate of convergence of dykstra s cyclic projections algorithm The polyhedral case.pdf
|   |       
|   \---Notes
|           C21_MPC_Lecture_Notes.pdf
|           C21_MPC_Problems.pdf
|           dykstra.pdf
|           
+---Latex
|   +---Current Version
|   |       0041555367901139.bib
|   |       DifferentSequences.png
|   |       Dykstra's Projection Algorithm.pdf
|   |       dykstra.pdf
|   |       dykstra.tex
|   |       dykstra.zip
|   |       dykstra_algorithm.py
|   |       dykstra_demonstration.png
|   |       Dykstra_wiki.png
|   |       hundred_corners_rounding.png
|   |       intermediate_steps.png
|   |       in_intersection_dykstra.png
|   |       in_intersection_MAP.png
|   |       in_intersection_modified.png
|   |       LQR + Riccati.pdf
|   |       main.tex
|   |       MAP_demonstration.png
|   |       MAP_one_corner.png
|   |       MAP_wiki.png
|   |       master_bib_abbrev.bib
|   |       master_bib_abbrev.bib.bak
|   |       MPC derivation of condensed form.pdf
|   |       mymath.sty
|   |       non_rounded_test.png
|   |       not_in_intersection_dykstra.png
|   |       not_in_intersection_modified.png
|   |       one_corner_rounding.png
|   |       qp-benchmark-2017.png
|   |       regions.png
|   |       rounded_test.png
|   |       stalling.png
|   |       StallingRegionsHand.png
|   |       
|   +---Idris Version
|   |       readme.txt
|   |       
|   \---Initial Version
|       |   0041555367901139.bib
|       |   DifferentSequences.png
|       |   does_not_stay_in_intersection.png
|       |   Dykstra's Projection Algorithm.pdf
|       |   dykstra.aux
|       |   dykstra.bbl
|       |   dykstra.blg
|       |   dykstra.log
|       |   dykstra.pdf
|       |   dykstra.synctex.gz
|       |   dykstra.tex
|       |   dykstra_algorithm.py
|       |   dykstra_demonstration.png
|       |   Dykstra_wiki.png
|       |   hundred_corners_rounding.png
|       |   intermediate_steps.png
|       |   in_intersection_dykstra.png
|       |   in_intersection_MAP.png
|       |   in_intersection_modified.png
|       |   LQR + Riccati.pdf
|       |   MAP_demonstration.png
|       |   MAP_one_corner.png
|       |   MAP_wiki.png
|       |   master_bib_abbrev.bib
|       |   master_bib_abbrev.bib.bak
|       |   MPC derivation of condensed form.pdf
|       |   mymath.sty
|       |   non_rounded_test.png
|       |   not_in_intersection_dykstra.png
|       |   not_in_intersection_modified.png
|       |   one_corner_rounding.png
|       |   qp-benchmark-2017.png
|       |   regions.png
|       |   rounded_test.png
|       |   stalling.png
|       |   StallingRegionsHand.png
|       |   
|       \---miscellaneous
|               Dykstra_Algorithm_notes.pdf
|               Dykstra_Algorithm___rough.pdf
|               error_visualisation.png
|               test.png
|               
\---Python
    +---Previous Versions
    |   +---Version 1
    |   |       main.py
    |   |       
    |   +---Version 2
    |   |   |   dykstra.py
    |   |   |   main.py
    |   |   |   plotter.py
    |   |   |   test.py
    |   |   |   test2.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           dykstra.cpython-311.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           plotter.cpython-311.pyc
    |   |           
    |   +---Version 3 (path plotter)
    |   |   |   dykstra.py
    |   |   |   edge_rounder.py
    |   |   |   hexatest.py
    |   |   |   main.py
    |   |   |   MAP.py
    |   |   |   MAP_demonstration.py
    |   |   |   path_plotter.py
    |   |   |   plotter.py
    |   |   |   test.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           demonstration.cpython-311-pytest-7.4.0.pyc
    |   |           dykstra.cpython-311.pyc
    |   |           edge_rounder.cpython-311.pyc
    |   |           hexatest.cpython-311-pytest-7.4.0.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           MAP.cpython-311.pyc
    |   |           path_plotter.cpython-311.pyc
    |   |           plotter.cpython-311.pyc
    |   |           
    |   +---Version 4
    |   |   |   dykstra.py
    |   |   |   edge_rounder.py
    |   |   |   gradient.py
    |   |   |   main.py
    |   |   |   MAP.py
    |   |   |   MAP_demonstration.py
    |   |   |   myplot.png
    |   |   |   new_dykstra.py
    |   |   |   old_main.py
    |   |   |   path_plotter.py
    |   |   |   plotter.py
    |   |   |   test gradient.py
    |   |   |   test plotter.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           dykstra.cpython-311.pyc
    |   |           edge_rounder.cpython-311.pyc
    |   |           gradient.cpython-311.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           new_dykstra.cpython-311.pyc
    |   |           old_main.cpython-311-pytest-7.4.0.pyc
    |   |           path_plotter.cpython-311.pyc
    |   |           plotter.cpython-311.pyc
    |   |           
    |   +---Version 5
    |   |   |   dykstra.py
    |   |   |   edge_rounder.py
    |   |   |   gradient.py
    |   |   |   main.py
    |   |   |   modified_dykstra.py
    |   |   |   path_plotter.py
    |   |   |   plotter.py
    |   |   |   test from AI.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           dykstra.cpython-311.pyc
    |   |           edge_rounder.cpython-311.pyc
    |   |           gradient.cpython-311.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           MAP_demonstration.cpython-311-pytest-7.4.0.pyc
    |   |           modified_dykstra.cpython-311.pyc
    |   |           path_plotter.cpython-311.pyc
    |   |           plotter.cpython-311.pyc
    |   |           test from AI.cpython-311-pytest-7.4.0.pyc
    |   |           
    |   +---Version 6
    |   |   |   dykstra.py
    |   |   |   edge_rounder.py
    |   |   |   gradient.py
    |   |   |   main.py
    |   |   |   modified_dykstra.py
    |   |   |   path_plotter.py
    |   |   |   plotter.py
    |   |   |   random test.py
    |   |   |   test beta.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           dykstra.cpython-311.pyc
    |   |           edge_rounder.cpython-311.pyc
    |   |           gradient.cpython-311.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           modified_dykstra.cpython-311.pyc
    |   |           path_plotter.cpython-311.pyc
    |   |           plotter.cpython-311.pyc
    |   |           random test.cpython-311-pytest-7.4.0.pyc
    |   |           test from AI.cpython-311-pytest-7.4.0.pyc
    |   |           
    |   +---Version 7
    |   |   |   dykstra.py
    |   |   |   edge_rounder.py
    |   |   |   gradient.py
    |   |   |   main.py
    |   |   |   modified_dykstra.py
    |   |   |   path_plotter.py
    |   |   |   plotter.py
    |   |   |   random test.py
    |   |   |   test beta.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           dykstra.cpython-311.pyc
    |   |           edge_rounder.cpython-311.pyc
    |   |           gradient.cpython-311.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           modified_dykstra.cpython-311.pyc
    |   |           path_plotter.cpython-311.pyc
    |   |           plotter.cpython-311.pyc
    |   |           random test.cpython-311-pytest-7.4.0.pyc
    |   |           
    |   +---Version 8
    |   |   |   dykstra.py
    |   |   |   edge_rounder.py
    |   |   |   gradient.py
    |   |   |   main.py
    |   |   |   modified_dykstra.py
    |   |   |   path_plotter.py
    |   |   |   plotter.py
    |   |   |   random test.py
    |   |   |   test beta.py
    |   |   |   
    |   |   +---.pytest_cache
    |   |   |   |   .gitignore
    |   |   |   |   CACHEDIR.TAG
    |   |   |   |   README.md
    |   |   |   |   
    |   |   |   \---v
    |   |   |       \---cache
    |   |   |               lastfailed
    |   |   |               nodeids
    |   |   |               stepwise
    |   |   |               
    |   |   \---__pycache__
    |   |           dykstra.cpython-311.pyc
    |   |           edge_rounder.cpython-311.pyc
    |   |           gradient.cpython-311.pyc
    |   |           main.cpython-311-pytest-7.4.0.pyc
    |   |           modified_dykstra.cpython-311.pyc
    |   |           path_plotter.cpython-311.pyc
    |   |           plotter.cpython-311.pyc
    |   |           random test.cpython-311-pytest-7.4.0.pyc
    |   |           
    |   \---Version 9
    |       |   data_generator.py
    |       |   dykstra.py
    |       |   edge_rounder.py
    |       |   gradient.py
    |       |   lil test.py
    |       |   main.py
    |       |   modified_dykstra.py
    |       |   path_plotter.py
    |       |   plotter.py
    |       |   random test.py
    |       |   stalling_destroyer.py
    |       |   tenDtest.py
    |       |   test beta.py
    |       |   test data generator.py
    |       |   
    |       +---.pytest_cache
    |       |   |   .gitignore
    |       |   |   CACHEDIR.TAG
    |       |   |   README.md
    |       |   |   
    |       |   \---v
    |       |       \---cache
    |       |               lastfailed
    |       |               nodeids
    |       |               stepwise
    |       |               
    |       \---__pycache__
    |               dykstra.cpython-311.pyc
    |               edge_rounder.cpython-311.pyc
    |               gradient.cpython-311.pyc
    |               main.cpython-311-pytest-7.4.0.pyc
    |               path_plotter.cpython-311.pyc
    |               plotter.cpython-311.pyc
    |               stalling_destroyer.cpython-311.pyc
    |               
    \---Working Version
        |   dykstra.py
        |   dykstra_functions.py
        |   dykstra_MAP_hybrid.py
        |   edge_rounder.py
        |   gradient.py
        |   main.py
        |   new_dykstra.py
        |   plotter.py
        |   
        +---.idea
        |   |   .gitignore
        |   |   misc.xml
        |   |   modules.xml
        |   |   vcs.xml
        |   |   Working Version.iml
        |   |   workspace.xml
        |   |   
        |   \---inspectionProfiles
        |           profiles_settings.xml
        |           Project_Default.xml
        |           
        +---.pytest_cache
        |   |   .gitignore
        |   |   CACHEDIR.TAG
        |   |   README.md
        |   |   
        |   \---v
        |       \---cache
        |               lastfailed
        |               nodeids
        |               stepwise
        |               
        \---__pycache__
                dykstra.cpython-311.pyc
                dykstra_functions.cpython-311.pyc
                dykstra_MAP_hybrid.cpython-311.pyc
                edge_rounder.cpython-311.pyc
                gradient.cpython-311.pyc
                main.cpython-311-pytest-7.4.0.pyc
                new_dykstra.cpython-311.pyc
                plotter.cpython-311.pyc
"
