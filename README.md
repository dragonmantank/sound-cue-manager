# Sound Cue Manager

The Sound Cue Manager is a Python application designed to simplify the management of sound cues for live performances. It provides a user-friendly interface to load and save sound cue lists, making it easy for audio technicians and live event producers to organize and execute sound cues seamlessly.

## How to Run

To run the Sound Cue Manager on your local machine, follow these steps:

1. Clone this repository to your computer:

   ```bash
   git clone https://github.com/dragonmantank/sound-cue-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sound-cue-manager
   ```

3. Install the required dependencies using pip:

   ```bash
   pipenv install
   ```

4. Run the application:

   ```bash
   pipenv run app
   ```

5. Follow the on-screen instructions to load and save sound cue lists.

## Contributing

We welcome contributions to improve the Sound Cue Manager. If you'd like to contribute, please follow these guidelines:

1. Fork the repository to your GitHub account.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your GitHub repository:

   ```bash
   git push origin feature-name
   ```

5. Create a pull request on the main repository.

6. Your pull request will be reviewed, and once approved, your changes will be merged.

## FAQ

### Q: How do I add new sound cues to the list?

A: Currently you will need to create a JSON file in the following format:

```json
[
    {
        "path": "path/to/file/with/forward/slashes.mp3",
        "title": "Title to show in list"
    }
]
```

You can then load this file into the application. It does not currently allow you to add or edit existing entries.

### Q: Can I import sound cue lists from other file formats?

A: Currently, the Sound Cue Manager supports importing and exporting cue lists in the above JSON format.