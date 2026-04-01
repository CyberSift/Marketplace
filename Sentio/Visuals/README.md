# Sentio Visuals

This folder contains the visuals for the Sentio platform.

## Expected Format

`metadata.json` should be a JSON array of objects with the following properties:

```json
[
  {
    "name": "Visual Name",
    "description": "Visual Description",
    "reference": "http://example.com/",
    "tags": ["tag1", "tag2", "tag3"],
    "export": {
        ... copy/paste the export object from the visual
    }        
  }
]
```

## Important

- The `name` property MUST be unique.
- Required properties are:
    - `name`
    - `export`    
- Use the `tags` property to categorize the visual and make it easier to find.
- The `reference` property is used to link to a more detailed description of the visual - usually a blog post or documentation page.