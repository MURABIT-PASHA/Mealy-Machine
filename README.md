Mealy Machine
=============

This project provides a graphical user interface for creating and visualizing Mealy machines.

Requirements
------------

To run this project, you will need to have the following dependencies installed:

-   Python 3
-   Tkinter
-   CairoSVG
-   webview

Usage
-----

To run the program, execute the following command:

```bash
python main.py
```

This will open the GUI window. To create a Mealy machine, enter the input alphabet and the number of states in the respective `Entry` widgets and click the "Create Scheme" button. This will generate a grid of `Entry` and `Combobox` widgets, where you can specify the output and next state for each input symbol and each state. When you have finished specifying the state transitions, click the "Create Diagram" button to generate a graphical representation of the Mealy machine. You can test strings by clicking the "Test String" button.

Features
--------

-   Generate a graphical representation of a Mealy machine.
-   Test strings to see the output and next state for each input symbol.

Screenshots
-----------

Insert some screenshots of the program here to give the user an idea of what the program looks like and how it functions.

Future Work
-----------

-   Add the ability to save and load Mealy machine configurations.
-   Implement a minimization algorithm for Mealy machines.
-   Add support for nondeterministic Mealy machines.

Acknowledgements
----------------

-   The `diagrams` library was used to generate the Mealy machine diagrams.
-   The `CairoSVG` library was used to convert the SVG button images to PNG format.
-   The `webview` library was used to open the LinkedIn and website links in the GUI.

Credits
-------

This project was developed by [Murabıt Akdoğan](https://murabit-akdogan.me/).

License
-------

This project is licensed under the terms of the MIT license.
