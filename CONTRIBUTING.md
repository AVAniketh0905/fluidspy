# Contribute to Fluidspy

Everyone is welcome to contribute, and we value everybody's contribution. Code
contributions are not the only way to help the community. Answering questions, helping
others, and improving the documentation are also immensely valuable.

TODO
Are you a developer? Check out the steps here to [contribute code](#contribute-code).

TODO
Are you a mechanical engineer? Check out the steps here to [contribute validation](#contribute-validation).

It also helps us if you spread the word! Reference the library in blog posts
about the awesome projects it made possible, shout out on Twitter every time it has
helped you, or simply ⭐️ the repository to say thank you.

However you choose to contribute, please be mindful and respect our
[code of conduct](https://github.com/AVAniketh0905/fluidspy/CODE_OF_CONDUCT.md).

**This guide was heavily inspired by the awesome [scikit-learn guide to contributing](https://github.com/scikit-learn/scikit-learn/blob/main/CONTRIBUTING.md).**

## Ways to contribute

There are several ways you can contribute to fluidspy:

- Fix outstanding issues with the existing code.
- Submit issues related to bugs or desired new features.
- Implement new algorithms.
- Contribute to the examples or to the documentation.

- Contribute to mechanical validation.
- Write detailed fluid dynamics explanations.

If you don't know where to start, there is a special [Good First
Issue](https://github.com/AVAniketh0905/fluidspy/contribute) listing. It will give you a list of
open issues that are beginner-friendly and help you start contributing to open-source. Just comment in the issue that you'd like to work on it.

> All contributions are equally valuable to the community!

## Fixing outstanding issues

If you notice an issue with the existing code and have a fix in mind, feel free to [start contributing](https://github.com/AVAniketh0905/fluidspy/CONTRIBUTING.md/#create-a-pull-request) and open a Pull Request!

## Submitting a bug-related issue or feature request

Do your best to follow these guidelines when submitting a bug-related issue or a feature
request. It will make it easier for us to come back to you quickly and with good
feedback.

### Did you find a bug?

TODO
The Fluidspy library is new and just starting out.

Before you report an issue, we would really appreciate it if you could **make sure the bug was not already reported** (use the search bar on GitHub under Issues). Your issue should also be related to bugs in the library itself, and not your code. If you're unsure whether the bug is in your code or the library, please ask on the [Discord](// TODO) first. This helps us respond quicker to fixing issues related to the library versus general questions.

Once you've confirmed the bug hasn't already been reported, please open a new issue bu using the Bug Report Template.

### Do you want a new feature?

If there is a new feature you'd like to see in fluidspy, please open an issue and describe:

1. What is the _motivation_ behind this feature? Is it related to a problem or frustration with the library? Is it a feature related to something you need for a project? Is it something you worked on and think it could benefit the community?

   Whatever it is, we'd love to hear about it!

2. Describe your requested feature in as much detail as possible. The more you can tell us about it, the better we'll be able to help you.
3. Provide a _code snippet_ that demonstrates the features usage.
4. If the feature is related to a paper, please include a link.

If your issue is well written we're already 80% of the way there by the time you create it.

We have added [templates](https://github.com/AVAniketh0905/fluidspy/.github/ISSUE_TEMPLATE) to help you get started with your issue.

## Do you want to implement a new algorithm?

New algorithms are constantly released and if you want to implement a new algorithm, please provide the following information

- A short description of the algorithm and link to the paper/ other informative source.
- Link to the implementation if it is open-sourced.

If you are willing to contribute the model yourself, let us know so we can help you add it to Fluidspy!

TODO
We have added a [detailed guide and templates](TODO) to help you get started with adding a new algorithm.

## Do you want to add documentation?

We're always looking for improvements to the documentation that make it more clear and accurate. Please let us know how the documentation can be improved such as typos and any content that is missing, unclear or inaccurate. We'll be happy to make the changes or help you make a contribution if you're interested!

## Create a Pull Request

Before writing any code, we strongly advise you to search through the existing PRs or
issues to make sure nobody is already working on the same thing. If you are
unsure, it is always a good idea to open an issue to get some feedback.

You will need basic `git` proficiency to contribute to `fluidspy`. While `git` is not the easiest tool to use, it has the greatest
manual. Type `git --help` in a shell and enjoy! If you prefer books, [Pro
Git](https://git-scm.com/book/en/v2) is a very good reference.

You'll need **[Python 3.10](<(https://github.com/AVAniketh0905/fluidspy/setup.py)>)** or above to contribute to fluidspy. Follow the steps below to start contributing:

1. Fork the [repository](https://github.com/AVAniketh0905/fluidspy) by clicking on the **[Fork](https://github.com/AVAniketh0905/fluidspy/fork)** button on the repository's page. This creates a copy of the code under your GitHub user account.

2. Clone your fork to your local disk, and add the base repository as a remote:

   ```bash
   git clone git@github.com:<your Github handle>/fluidspy.git
   cd fluidspy
   git remote add upstream https://github.com/AVAniketh0905/fluidspy.git
   ```

3. Create a new branch to hold your development changes:

   ```bash
   git checkout -b a-descriptive-name-for-my-changes
   ```

   🚨 **Do not** work on the `main` branch!

4. Set up a virtual environment by running the following command:

   ```bash
    python -m venv .venv
   ```

5. Set up a development environment by running the following command in a virtual environment:

   ```bash
   pip install -r requirements_dev.txt
   pip install -e fluidspy
   ```

   If `fluidspy` was already installed in the virtual environment, remove
   it with `pip uninstall fluidspy` before reinstalling it in editable
   mode with the `-e` flag.

6. Develop the features on your branch.

   As you work on your code, you should make sure the test suite
   passes. Run the tests impacted by your changes like this:

   ```bash
   pytest fluidspylib/
   ```

   For more information about tests, check out the guide.

   Fluidspy relies on `black` and `ruff` to format its source code consistently. After you make changes, apply automatic style corrections and code verifications that can't be automated in one go with:

   - Ruff (type checking):

   ```bash
    // TODO
   ```

   - Black (code formatting):

   ```bash
   // TODO
   ```

Once you're happy with your changes, add changed files with `git add` and
record your changes locally with `git commit`:

```bash
git add modified_file.py
git commit
```

Please remember to write [good commit
messages](https://chris.beams.io/posts/git-commit/) to clearly communicate the changes you made!

To keep your copy of the code up to date with the original
repository, rebase your branch on `upstream/branch` _before_ you open a pull request or if requested by a maintainer:

```bash
git fetch upstream
git rebase upstream/main
```

Push your changes to your branch:

```bash
git push -u origin a-descriptive-name-for-my-changes
```

If you've already opened a pull request, you'll need to force push with the `--force` flag. Otherwise, if the pull request hasn't been opened yet, you can just push your changes normally.

1. Now you can go to your fork of the repository on GitHub and click on **Pull request** to open a pull request. Make sure you tick off all the boxes in our [checklist](https://github.com/AVAniketh0905/fluidspy/blob/main/CONTRIBUTING.md) below. When you're ready, you can send your changes to the project maintainers for review.

2. It's ok if maintainers request changes, it happens to our core contributors too! So everyone can see the changes in the pull request, work in your local branch and push the changes to your fork. They will automatically appear in the pull request.

### Pull request checklist

- [ ] The pull request title should summarize your contribution.
- [ ] If your pull request addresses an issue, please mention the issue number in the pull request description to make sure they are linked (and people viewing the issue know you are working on it).
- [ ] To indicate a work in progress please prefix the title with `[WIP]`. These are useful to avoid duplicated work, and to differentiate it from PRs ready to be merged.
- [ ] Make sure existing tests pass.
- [ ] If adding a new feature, also add tests for it.

TODO

- If you are adding a new algorithm, make sure you use //TODO
- **Github Actions runs some basic tests!**

- [ ] All public methods must have informative docstrings (see
      [`example.py`](link to example // TODO)
      for an example).

TODO
For more information about the checks run on a pull request, take a look at our `Checks on PRs` guide.

### Tests

An extensive test suite is included to test the library behavior and several examples. Library tests can be found in
the [tests](https://github.com/AVAniketh0905/fluidspy/tree/main/fluidspylib/fluidspy/tests) folder.

We like `pytest` because it's faster. From the root of the
repository, specify a _path to a subfolder or a test file_ to run the test.

```bash
python -m pytest fluidspylib/
```

You can also specify a smaller set of tests in order to test only the feature
you're working on.

Fluidspy uses `pytest` as a test runner only.

### Style guide

For documentation strings, fluidspy follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
Check our [documentation writing guide](// TODO) for more information.

### Sync a forked repository with upstream main (the Fluidspy Face repository)

When updating the main branch of a forked repository, please follow these steps to avoid pinging the upstream repository which adds reference notes to each upstream PR, and sends unnecessary notifications to the developers involved in these PRs.

1. When possible, avoid syncing with the upstream using a branch and PR on the forked repository. Instead, merge directly into the forked main.
2. If a PR is absolutely necessary, use the following steps after checking out your branch:

```bash
git checkout -b your-branch-for-syncing
git pull --squash --no-commit upstream main
git commit -m '<your message without GitHub references>'
git push --set-upstream origin your-branch-for-syncing
```
