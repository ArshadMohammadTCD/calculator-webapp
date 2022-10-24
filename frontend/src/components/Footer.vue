<template>
    <MDBFooter :text="['center', 'lg-start']">

        <div class="fixed-bottom text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
            <a class="text-dark">
                Developed by Wesley Shaw, Abigail Amethyst, Paddi Hua and Arshad Mohammed for CSU33012
            </a>
        </div>
        <!-- Copyright -->
    </MDBFooter>
</template>

<script>
export default {
    name: 'AppFooter',
    props: {
        msg: String
    }
}
</script>

<style>

</style>