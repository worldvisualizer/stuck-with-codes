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