<!--
@component

The footer that is on every page.
-->
<script lang="ts">
  let { page = '' } = $props();
  let homepage = '<a class="pages" href="/">Homepage</a>'
  let pages = ['VS Char', "Chars Adventure", "Site Archive", "Blogs", "Credits", "Official Games"]

  let pages_html = get_pages(gen_pagesArray())
  let promo = get_pages([`<a class="socials" href="https://yt.vschar-official.com" target="_blank" rel="noopener noreferrer" class="footer">My Youtube Channel</a>`,
        `<a class="socials" href="https://bsky.vschar-official.com" target="_blank" rel="noopener noreferrer" class="footer">My BlueSky Account</a>`,
        `<a class="socials" href="https://twitch.vschar-official.com" target="_blank" rel="noopener noreferrer" class="footer">My Twitch Channel</a>`,
        `<a class="socials" href="https://discord.vschar-official.com" target="_blank" rel="noopener noreferrer" class="footer">My Discord Server</a><br>`,])

  function get_pageName(element:string)
  {
    return element.split(">")[1].split("<")[0]
  }

  function gen_pagesArray():Array<string>
  {
    let array:Array<string> = []
    pages.forEach(page => {
        let pageToGet = ""
        switch (page)
        {
            case "VS Char": pageToGet = "/vschar";
            case "Chars Adventure": pageToGet = "/charsadventure"; page = "Char's Adventure";
            case "Site Archive": pageToGet = "https://old.vschar-official.com";
            case "Official Games": pageToGet = "/games"
            default: pageToGet = page.toLocaleLowerCase().replaceAll(" ", ""); // Not in this list.
        }

        array.push('<a class="pages" href="'+pageToGet+'">'+page+'</a>')
    });

    return array;
  }

  function get_pages(array:Array<string>)
  {
    let finalHTML = ""
    let pos = 0
    array.forEach(element => {
        if (element != "")
        {
            pos++;
            if (page == element)
            {
                element = homepage
            }

            finalHTML += element
            if (pos < array.length) finalHTML += " | "
        }
    });

    return finalHTML
  }
</script>

<main class="FooterClass">
    <div class="footer">
        <div class="pages">
            {@html pages_html}
        </div>
        <div class="socials">
            {@html promo}
        </div>
        <div class="sitemap"><a href="/sitemap">Site Map</a></div>
        <div class="copyright">© Char Golden Games 2026</div>
    </div>
</main>

<style>
    .footer
    {
        margin-top: 80px;
        position: fixed;
        bottom: 0;
        left: 0;
        background-color: #00000085;
        width: 100%;
        align-items: center;
        align-content: center;
        text-align: center;
    }

    .pages
    {
        color: #FF8800;
        margin: auto;
        margin-top: 40px;
        max-height: 20px;

        &:hover {
            color: #FFCC66
        }

        &:link
        {
            color: #FFAA22
        }

        &:visited
        {
            color: #AA4400;
        }
    }

    .socials
    {
        color: #FFFFFF;
        margin: auto;
        margin-top: 40px;
        max-height: 20px;

        &:link {
            color: #00AAFF;
        }

        &:hover {
            color: #88EEFF;
        }

        &:visited {
            color: #44DDFF;
        }
    }
    
    .sitemap
    {
        margin-top: 40px;
        margin-right: 40px;
        max-height: 20px;
    }
</style>