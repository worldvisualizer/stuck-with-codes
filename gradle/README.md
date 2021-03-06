### Projects and Tasks

- Everything in Gradle is either project or task.
- Every gradle build is made up of one or more projects.
    - could be JAR, web app, ZIP, etc.
- Each project is made up of one or more tasks
- Task: some atomic piece of work performed by build.

### How is the Gradle Project Organized

├── build.gradle                      # build script
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar        # executable jar
│       └── gradle-wrapper.properties # config properties
├── gradlew                           # wrapper script for unix
└── settings.gradle                   # settings for build config

### Gradle has Plugins

- plugins like docker are used for easy task configurations

### Adding Task

```
task zip(type: Zip, group: "Archive", description: "Archive zip") {
	from "src"
	archiveFileName = "toy-1.0.zip"
}
```

### Gradle has Properties

```
./gradlew properties
```
- you can specify some of the configs here

### What does Gradle Build do?

- first time to build: check dependency cache and download if absent in `.gradle` directory
- compiles classes
- runs the tests
- generates test report
- if build successful, resulting jar in `build/libs`