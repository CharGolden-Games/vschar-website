<!--
@component

The footer that is on every page.
-->

<main class="FooterClass">
    <div class="footer">
        <div class="pages">
            Test Item 1
        </div>
        <div class="socials">
            Test Item 2
        </div>
        <div class="sitemap"><a href="/sitemap">Site Map</a></div>
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
        width: 150%;
    }

    .pages
    {
        color: #FF8800;
        margin-top: 40px;
        max-height: 20px;
    }

    .pages:link
    {
        color: #FFAA22
    }

    .pages:hover
    {
        color: #FFCC66
    }

    .pages:visited
    {
        color: #AA4400;
    }

    .socials
    {
        color: #FFFFFF;
        margin-top: 40px;
        max-height: 20px;
    }

    .socials:link
    {
        color: #00AAFF;
    }

    .socials:hover
    {
        color: #88EEFF;
    }

    .socials:visited
    {
        color: #44DDFF;
    }
    
    .sitemap
    {
        margin-top: 40px;
        max-height: 20px;
    }
</style>