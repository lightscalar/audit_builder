# Getting this system installed.

This is a quick guide on what needs to be installed in order to get the PDF
generator up and running. This is done in the context of a Mac, but
instructions can be found for installing software on Windows and Linux systems.

## Install necessary libraries

We are using the _weasyprint_ library, documentation for which can be found
[here](https://weasyprint.org/).

```shell
brew install weasyprint
```

And add the corresponding Python libraries:

```shell
pip install -r requirements.txt
```

Next, install the tailwindcss CLI according to instructions
[here](https://tailwindcss.com/docs/installation). This CLI will allow us to
use tailwindcss in our HTML and CSS files and make everything look nice.

