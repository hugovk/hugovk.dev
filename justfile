# Create a new blog post
new title:
    #!/usr/bin/env bash
    year=$(date +%Y)
    slug=$(echo "{{ title }}" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
    hugo new content "blog/${year}/${slug}/index.md"
