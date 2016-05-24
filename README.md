
## OpenIntents Website

Between 2008 and 2015 the website was using drupal. Since then Github pages are used to 
decrease the maintance work. The focus is on Intent specifications.

## Intent Specification for Writers
An Intent protocol is defined in a file in folder _intent_specs. The file has to be named as
&lt;action name>.md. 

[Start writing by creating a new file](https://github.com/openintents/openintents.github.io/new/master/_intent_specs)

The YAML frontmatter can contain the following properties

Property | Description
 --------| -------
 `title` | Title of the intents protocol
 `action` | Action name as it has to be placed in the manifest (same as file name without .md)
 `constant` | Java constant that can be used in source code instead of a string, e.g. `android.content.Intent.ACTION_VIEW`
 `uri` | Description what the data uri should contain
 `extras` | List of extras
 `out` | Description of the return value, uri and list of extras returned
 `link` | Link to a website that describes the intent protocol as well or the use of it
 `component` |  `activity` (default) or `service` or `receiver`
 `webintent` |  Url of the web intent equivalent to the Android intent
 `webwish` | Url of the web wish equivalent to the Android intent
 `ios` | Name and link to ios extension equivalent to the Android intent
 `author` | Author of the specification 
 `submitted` | Date when the specification was submitted to openintents.org
 `hide_use` | flag to hide the auto-generated use section in the documentation (should be true for `service` and `receiver`)
 `hide_intent_filter` | flag to hide auto-generated intent filter example in the documentation
 `permalink` | must be set by `service` and `receiver` intents as well as specializations of intents (see below)
 `implemenations` | List of apps implementing the specification
 `name` | Name of specialization of intent (should not be used by main specification)

*Extras* are defines with the following properties:

Property | Description
 --------| -------
 `name` | Name of extra as it is used as the key
 `type` | Java type of extra
 `description` | Description of the content of extra
 `sample` | Value that should be used as part of the documentation to launch the intent
 `var` | Java variable name that should be used as part of the documentation to handle the result value

*Implementations* are defined with the following properties:

Property | Description
 --------| -------
 `name` | Name of the app
 `url` | Url to app store or website of app

### Specializations of intent specs
Intent specifications are defined by its intent action. If there are intents that use e.g. different schema and have different behaviour these intent can be documented separately.

The path is action/[action]/[name], e.g. http://www.openintents.org/action/android-intent-action-view/x11-server

The name of the file should match the name property. Name clashes with the main specification must be avoided.

## OI Apps
See https://openintents.org/download for all apps and more.
