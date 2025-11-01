# Robots and Coffee Co.

This is the repository for the Robots and Coffee Co. website.

## Tips for managing content

### Attaching images

When creating the file, simply paste the image normally with `cmd+v`, after the post is done, do a find an replace of `content/` for `{static}/`.

This will break the visualisation in Obsidian but enable Pelican to render the image properly.

Using the Obsidian style of attaching images (both the markdown with `![]()` and obsidian wikilinks `[[]]`) fail due to path differences in how Obsidian and Pelican look for images. I've tries unsuccessfully using this pelican plugin [Obsidian: A Plugin for Pelican - GitHub](https://github.com/jonathan-s/pelican-obsidian), but it is worth deep diving into it or checking out other things that the community has to offer.

### Attaching Local Videos

Manually move the `.mp4` file to the `content/videos/` folder. Then, in the article page, add the code bellow targeting the path of the video file.

```
<video autoplay loop muted playsinline style="max-width: 100%; height: auto;">
  <source src="/videos/my-video-file.mp4" type="video/mp4">
</video>
```

The video will keep playing in repeat similar to a gif. Obsidian will not be able to render that in the editor, so the code will disappear when the cursor is not on top of it. If that is annoying, you can temporarily add code style to it and remove latter, so that pelican can render the HTML.

## To Do's

- [ ] Find a better way to attach images that work in both Pelican and Obsidian

