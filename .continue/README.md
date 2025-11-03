# Continue Configuration

This directory contains the configuration for the [Continue](https://continue.dev/) AI coding assistant.

## Setup

1. Install the Continue extension in your IDE:
   - **VS Code**: Install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Continue.continue)
   - **JetBrains IDEs**: Install from the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/22707-continue)

2. Add your API keys to `config.json`:
   - For OpenAI models (GPT-4, GPT-3.5): Add your OpenAI API key
   - For Anthropic models (Claude): Add your Anthropic API key
   - For Mistral models (Codestral): Add your Mistral API key

3. Configure your preferred models by updating the `apiKey` fields in `config.json`

## Features Configured

### Models
- **GPT-4**: Advanced reasoning and code generation
- **GPT-3.5 Turbo**: Fast responses for general coding tasks
- **Claude 3**: Alternative powerful model for code generation

### Tab Autocomplete
- **Codestral**: Optimized for code completion

### Context Providers
- **code**: Reference code from your codebase
- **docs**: Access documentation
- **diff**: View git diffs
- **terminal**: Reference terminal output
- **problems**: View linter/compiler errors
- **folder**: Browse project structure
- **codebase**: Search across entire codebase

### Custom Commands
- **/test**: Generate comprehensive test suites using React Testing Library and Jest

### Documentation
- React Documentation
- Create React App Documentation

## Security

⚠️ **Important**: Never commit your API keys to version control. The `config.json` file should have empty `apiKey` fields in the repository. Add your keys locally after cloning.

Consider using environment variables for API keys in CI/CD environments.

## Usage

Once configured, you can:
- Use `Cmd/Ctrl + L` to open the Continue chat
- Use `Cmd/Ctrl + I` to edit code inline
- Type `/` in the chat to see available slash commands
- Use Tab for AI-powered autocomplete
- Select code and right-click to access Continue commands

## Customization

You can customize the configuration by editing `config.json`:
- Add or remove models
- Configure different context providers
- Create custom slash commands
- Add project-specific documentation sources
