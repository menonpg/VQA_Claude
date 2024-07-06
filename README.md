# Visual Question Answering (VQA) using Claude

<p align="center">
    <a href="https://claude.ai/" title="Go to claude.ai">
        <img src="https://img.shields.io/badge/CLAUDE%20AI-cc785c?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABnCAYAAAD2duf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAACZtJREFUeNrsXd1t20gQXgmHAPcUXgWhKzBVQagKTqrgqApiVSCrAssVyFeBlAokV2C6AisVhHk6IC85rjJ0Fgy5M7N/pCwNQAiG+bPLb2fmm9ndoRAXuchF2mUQ8mHfv/+XlD8T+PNQHe/e/Xm4QBFYSjCy8vjRcqzLIwrQhuiCxM8XEZfHVw0g8njy/PwdtEGCH5+1yYKXnRBOnZbma+v42Tflz6I8VO0oymPUR1M5DADGHREMKZ8cPzstf+5qYAj4e91HDRkGeMYN49zUsTn5B3nW7TkCwpWFQweeIad9PEdAcub5mSM2lBHOebwA4t7Mtck14ZzDOQLy2eAaF849vgDSLHuDayIZSFo+N/KkvW8iDrkzMEMypXJl8cwfyClFef+/LPulpoIq2Zb3zfsOiBytL8RRq8q47NzeEyD78t5jy4DzrsUMyqCz6C3thcbNQlFgIks7WICxbgGj8l3GQWewOARSItzRnoJZ4Arlmi8WYGD+bVKeNzmFwNBESz55asveAIxbYnwjxSiDHRQQSOYtDQLFmHmNc8oLrI9jQiMGeJ1piJSV+JltdR11cwApOJleAMPEL2x7Dwg4+DnXbDmeXMoZYKSGYBjNhA4ZDUuUSaYnmPDZQIO5oDwwbXjEjGM+IP9/pPa5/NkYgm40rzMkNky+kJ0SR8iGphAU7QzT2FxfsmD4kthWQ+BZO4PYiQU6G5AGMNpe1oZjViDgewgRl3AdOvRjYwFGbjrzOSAAkgIg1I5OqakDGIVPzI5fYbZZmlbdPcvrBw5ijVbCABmG3JfJ4jCi4wumJgbhxd570JLINP6AlEhmoX0zm1zWkPDSTG6+pi7tKe9/y4wJtHEJwc/kiDW4swBjabtIg8qyTEDJwOFTHPHcoZZgz3vWALmxeJd7GFwiBCB7w/snYMImiJZw81w6LYm4g8uBEz/6ThdsgwrIUphP5hw7S6DGS0dakhiYYM5SpSaZmqbbjQCBh42F3QzbAoLJyBENNslx5X1z4saRugSlPEYGI1kV6TRfNNE9995NKY2PVEAgErdx4g+QdRDBAamxopGlCdvBtG4TDeaAkjJTN88NfsNUcgMy4h4QxQ5LE7ayePYN5MTqZoebDV4wWFZe067YsO2FS79hDYhiwubALkwb9hsLg07aaAkKCPiNicV7m/laqO1kkQOM8jX4CFNZQWBVwD1fGCP4dcGCZnHDcRUL+A2brQ8rGIiit4AowNwKuwRgXrEW0BqOja+W9Hxt+b+MdeQUssnqF7V9Yx+mytpkeXL4CTj8zCBYnCCxBCVrjfmNmU8wnANSOXxLenzcuwEZV45p+JtAuW2Cv7nLeCOIyWowYQn4lsRiVEaMc6eCPlXAjTdmIoCEWrlo61s4OaXYwz1Hvk1VUEBqUXEqTkuMl7MirDSBQwK9rWj0IHTvWjZh9lVs1/9G4tf6gw+gvW0DUqZgloMueukobgkhV9QAEILTGI6PAAR30BWDLnsb0LeYyLJtwgkGlATgWtGA0/IhHpmYDylAO4qa2TEd+aehIT3WlhzYVeKBtWnTMoM+2YieaktQnzWo2cWsNkoq7l2EiFJPxLf40EZJqx9lumgALyATzSUodMGSyj4ea/ZXBc8ITGVdbfxWAQBaXfzm1BnFYZzxe6Vx31QQ1SBMmdVLT/TlH6Bfz9DnHIv4/+iooWntV9WMuhbGb/Xlt9JeMA82qelzFK3psY5DLHYJnYuoL3/v6yGDmrnIIPiJPQdAfZeiBkAwhkmOQ5SIVZWohQy8R0hCX8F+AB/wECrd3rvUSQv4qrO3XebpihFWjvsLUcNUrSI7+EGf7QYAsxFvy3SqMZwEbamC1VcNiSFSz87AX0lwZhVR6Fsuq9pt++kMCcUx3d+nbG8meOkb1yKXHX0Glpl2FJBO+zAfkgq7dbYu5XVVojIJFRKg7uZDLKZxc8+sq3HJD5hTFSAvbehikUMEpikzAGIeiAaj67AaZhLTkwME5jm4DltSwnvp8AJnpdmL48D8yuMafrn+cB9qoVwGNJZrh/dACQ+Wm/mDgVLrd30uPtb0U7Ksve+lpCkAwVXnAhq4UjRrgTCkSPiZN9kKR4usG4jCoQLCq8mCB0tbb7Ip5lUrFO1aI4GVXMz24nFsed+G4A0Qi/nwarn/tqby2DzNSPzaaiA8gzL1/YmLoUMgEnC6C0OzcFUDo/qkRIREt7nGVK0EvWwHdl61/S7pPSCgFSYM6ACjrmkDJUZv1VIW71vOkfMZVKf8r8D3o1Q7iJNeAgKfEjLVCjl6R03FWsBvZIh5m9ZGb+N54DApBWEWlVkS+k2skWBUPAoGCKxiN9UK6SDnTU5SWSynkzrrwdpA3Ym1BlIxFvjO4rUPUIYGQMhC+TthlgistGKviX6xjZ6rBq3SlevgFCSQ7HABfulK4Hsl1zAwu2FZSrk/rla87q5F7r9BqHK1f7Ee6+xaABnU2v5EDE6Pm3QYaR5nW964GpIYgCGZ0IgABraZv+431FHddr4KDqc87bH4GhRHmBG0K4NMQnBAUqZWjChFvYiV3OYtMUCseX5dY6hbrWOVqEAfZiFA8VFIuYCXN6IsnyFWctNV3eF+2IuqJTfqYgt4/ghx9pmuBJUPQLZIg/agFZyiNNgiBqzqTsIJ9GCQLDmmq3YtxsBSiFUi74A0NKhaTrkCpz1m1lTH9oJoqyeAdrV1/IumH7eCVm0irsdYRAaW2IDSiSAfK66ODLnHRHPtLSHV84N4pC33uMO+78uN6ocdgUEJ/ijV2sjV41yaLuUeWHmqhJtqGXYABiX4OxCdL2buMBNsbLpqzE1XcCcSjDKCXWgIZVcUtVpbagOIDeuqgXKAgHVlMHC6AwTqLGKxzJxIl03KwbalV6isUFutW2PCot4BAg4ay/tsGZTZZQp8KWjzJq2mCzFhy14BQizHmgveR8OuER/EofOcz/rdYJVQFRM2FZqKEJ0AQpz5ky+QO2eduAJEMV3Ukbwg3nPLrQcfQkMWBDZkUnI1dd1QBuvq54whQTtSxG8YffyEwOtttqBRyt5GJwkIoto2X6LBAPlmoSWkGMig7nwvANGNpLHFZsprn42GDAE2D3+SgLSNZNsvCmD+Y++g7TOEHBxOEZCmTs0cfFHA+4JrDRU+iPbJMmsJudhampl7244Qvxp35fKFAYk4Fqy0/cZULwBxDO4tIVo+uX4FT504lGvxhuUUAXn2GINcADEQLPlYXAAJKMB+dCztUVwkuGOPYLlNfQ77Ul6qa8Ylv8QDiw3iyxu5iHP5X4ABAN2Yg3caniOCAAAAAElFTkSuQmCC" alt="Claude AI">
    </a>
</p>


<p align="center">
    <a href="/">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RMNCLDYO/claude-ai-toolkit/main/.github/anthropic-logo-dark.png">
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RMNCLDYO/claude-ai-toolkit/main/.github/anthropic-logo-light.png">
          <img alt="Claude AI" width="200" src="https://raw.githubusercontent.com/RMNCLDYO/claude-ai-toolkit/main/.github/anthropic-logo-light.png">
        </picture>
    </a>
</p>

## Overview

VQA_Claude is an extension of the Claude AI Toolkit (see: https://github.com/RMNCLDYO/claude-ai-toolkit), offering advanced Visual Question Answering capabilities with multi-page PDF analysis using Claude 3.5 Sonnet at its backend, via a simple Streamlit app interface. The Claude AI toolkit itself is designed to be user-friendly and highly adaptable, making it suitable for both beginners and advanced users. With the integration of the Streamlit app, users can easily interact with the Anthropic's models for text generation and vision analysis.

## Key Features
- **Streamlit App**: User-friendly interface for interacting with the toolkit.
- **Conversational AI**: Create interactive, real-time chat experiences (chatbots) or AI assistants.
- **Image Captioning**: Generate detailed descriptions and insights or create captions from images.
- **Text Generation**: Produce coherent and contextually relevant text and answers from simple prompts.
- **PDF Analysis**: Analyze multi-page PDFs using Visual Question Answering techniques.
- **Highly Customizable**: Tailor settings like streaming output, system prompts, sampling temperature and more to suit your specific requirements.
- **Lightweight Integration**: Efficiently designed with minimal dependencies, requiring only the `requests` package for core functionality.

## Prerequisites
- `Python 3.x`
- An API key from Anthropic

## Dependencies
The following Python packages are required:
- `requests`: For making HTTP requests to the Claude API.
- `python-dotenv`: For managing API keys and other environment variables.
- `streamlit`: For the web interface.
- `PyMuPDF (fitz)`: For PDF processing.

## Installation
To use VQA_Claude, clone the repository to your local machine and install the required Python packages.

Here's the formatted content to match a README file for a Git repository:

# VQA_Claude

## Clone the Repository

```bash
git clone https://github.com/menonpg/VQA_Claude.git
```

## Navigate to the Repository Folder

```bash
cd VQA_Claude
```

## Install the Required Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Obtain an API key from Anthropic.

You have three options for managing your API key:

<details>
<summary>Click here to view the API key configuration options</summary>

### Setting it as an Environment Variable on Your Device (Recommended for Everyday Use)

1. Navigate to your terminal.
2. Add your API key like so:

    ```bash
    export CLAUDE_API_KEY=your_api_key
    ```

This method allows the API key to be loaded automatically when using the wrapper or CLI.

### Using an .env File (Recommended for Development)

1. Install `python-dotenv` if you haven't already:

    ```bash
    pip install python-dotenv
    ```

2. Create a `.env` file in the project's root directory.
3. Add your API key to the `.env` file like so:

    ```bash
    CLAUDE_API_KEY=your_api_key
    ```

This method allows the API key to be loaded automatically when using the wrapper or CLI, assuming you have `python-dotenv` installed and set up correctly.

### Direct Input

If you prefer not to use a `.env` file, you can directly pass your API key as an argument to the CLI or the wrapper functions.

**CLI**

```bash
--api_key "your_api_key"
```

**Wrapper**

```python
api_key="your_api_key"
```

This method requires manually inputting your API key each time you initiate an API call, ensuring flexibility for different deployment environments.

</details>

## Usage

### Streamlit App

The Streamlit app provides a user-friendly interface for both text generation and vision analysis.

#### Launching the App

To start the Streamlit app, run:

```bash
streamlit run app.py
```


## Examples

Below are some examples from the `samples/` folder of the repository. The outputs are based on the prompt asked in the `streamlitUI.png` on the following PDF: `samples/TestPDF.pdf`.

### Streamlit UI

![Streamlit UI](samples/streamlitUI.png)

### Output Part 1

![Output Part 1](samples/output_part1.png)

### Output Part 2

![Output Part 2](samples/output_part2.png)