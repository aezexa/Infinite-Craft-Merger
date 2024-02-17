# infinite-craft-merger
Export your Infinite Craft data from phone and import them to PC


# Step 1: Export from Mobile (Chrome for now)
1. Go to Settings > About Me > Enable Developer Mode.
2. Enable USB Debugging.
3. Open Chrome on PC.
4. Type `chrome:/inspect#devices` in the URL Bar
5. Click `Inspect` on the `neal.fun` website.
6. You can see your phone now, you can swipe on it, you can interact on it from PC!
7. Locate `console` tab in the inspect element section.
8. Copy paste this script into the console section:
```javascript
console.log(
  JSON.stringify(
    {
      discoveries:
        window.$nuxt.$root.$children[2].$children[0].$children[0]._data.discoveries,
      elements:
        window.$nuxt.$root.$children[2].$children[0].$children[0]._data.elements
    }
))
```
![image](https://github.com/aezexa/infinite-craft-merger/assets/59202286/24fd13f0-f34f-4f8a-a138-0566d738b3a4)
9. Copy the output and paste it into `mobile.json` in this repo.

# Step 2: Export from PC
1. Download [Violent Monkey](https://violentmonkey.github.io/get-it/).
2. Download [Infinite Craft Helper](https://github.com/Mikarific/InfiniteCraftHelper/raw/main/dist/InfiniteCraftHelper.user.js)
3. Refresh the Infinite Craft page on PC
4. Click the new Settings Icon (⚙️) besides the search bar.
5. Click "Export Save File".
6. Save it into `infinitecraft.json`.

# Step 3: Run the `main.py` script.
1. It will try to load the mobile JSON and the PC JSON, and merge the new phone items into the PC.
2. Note that it will not find the recipes for now. And it will simply load the items into PC.

# Step 4: Import the generated file `infinitecraft2.json` in the new Settings Icon (⚙️) besides the search bar.
1. Have fun! :)


Let me know if you wanted to collab!
