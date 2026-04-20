# Robots and Coffee Co.

This is the repository for the Robots and Coffee Co. website.

## Development Workflow

**Running locally**

1. Activate the environment with

```bash
. scripts/dev-activate
```

2. Run locally with

```bash
. scripts/dev-run
```

Access on http://127.0.0.1:8000

## Tips for managing content

### Attaching images

When creating the file, simply paste the image normally with `cmd+v`, after the post is done, do a find an replace of `content/` for `{static}/` with `opt + cmd + F`.

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

### Attaching YouTube Videos

Paste the code bellow in the article and replace the video URL with the one YouTube generates when selecting `share > embed` – this is different than the plain video URL.

```
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
  <iframe 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/VIDEO_ID" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
  </iframe>
</div>
```

## To Do's

- [ ] Find a better way to attach images that work in both Pelican and Obsidian
- [ ] Move `version-2` branch to `main` and update script code with it. Maybe change `source` to `production` or just `prod`

