<script>
    import { page } from "$app/state"
    import FooterClass from "../webpack/footer.svelte";
    let extPage = "ErrorPage"
</script>

<header>
    <title>
        VS Char Website | Error Page
    </title>
</header>

<main class="ErrorPage mainBody">
    Error!<br>

    {page.status + " " +  page.error?.message}

    <FooterClass page={extPage}/>
</main>

<style>
    @font-face {
  font-family: funkin;
  src: url('/fonts/funkin.ttf');
}

.footer {
    font-weight: bold;
    color: tan;
    font-size: medium;
}

a:link {
    color: tan;
}
  
a:active {
    color: tan;
}
  
a:visited {
    color: tan;
}
  
a:hover {
    color: blanchedalmond;
}

.box {
  background: #82aaff;
  max-width: 60vw;
  justify-content: center;
  align-items: center;
  flex-flow: row wrap;
  margin: auto;
  min-height: 57vh;
}

.box_title {
  background: #262238;
  min-height: 5vh;
  max-height: 5vh;
  max-width: 79vw;
  margin: auto;
}

.box_window {
    background: #887eb5;
    min-height: 50vh;
    max-width: 79vw;
    margin: auto;
}
.box_content {
  text-align: left;
  margin-left: 0;
  justify-content: left;
}
  
.hide {color: transparent;}
.small {font-size: small;}
.x-small {font-size: x-small;}
.xx-small {font-size: xx-small;}

.mainBody {
    background-image: url("/images/backgrounds/default/404.png");
    background-size: cover;
    color: black;
    min-height: 100vh;
  }
  
  .dumbHeader {
    font-style: italic;
    color: blanchedalmond;
  }
  
  body {
    background-image: url("/images/backgrounds/default/404.png");
    background-size: cover;
    color: white;
    text-align: center;
    font-weight: bold;
    font-size: x-large;
    margin: auto;
    padding-bottom: 30vh;
    font-family: funkin;
  }
</style>