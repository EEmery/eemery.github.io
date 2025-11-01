# Robots and Coffee Co.

This is the repository for the Robots and Coffee Co. website.

## Tips for managing content

### Attaching images

When creating the file, simply paste the image normally with `cmd+v`, after the post is done, do a find an replace of `content/` for `{static}/`.

This will break the visualisation in Obsidian but enable Pelican to render the image properly.

Using the Obsidian style of attaching images (both the markdown with `![]()` and obsidian wikilinks `[[]]`) fail due to path differences in how Obsidian and Pelican look for images. I've tries unsuccessfully using this pelican plugin [Obsidian: A Plugin for Pelican - GitHub](https://github.com/jonathan-s/pelican-obsidian), but it is worth deep diving into it or checking out other things that the community has to offer.

## To Do's

- [ ] Find a better way to attach images that work in both Pelican and Obsidian

