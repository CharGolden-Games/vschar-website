<script>
    import { page } from '$app/state';
    import FooterClass from "../webpack/footer.svelte";
</script>

<main>
    Error!<br>
    
    {page.status} {page.error?.message}

    <FooterClass page={"ErrorPage"}/>
</main>