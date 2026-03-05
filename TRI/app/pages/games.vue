<template>

<div class="cont">
    <gameSearchComp></gameSearchComp>

    <div class="games">
        <gameComp v-for="game in GAMES" :game="game"></gameComp>
    </div>
</div>



</template>


<script setup>
import gameSearchComp from '~/components/gameComp/gameSearchComp.vue';
import gameComp from '~/components/gameComp/gameComp.vue';
import { GAMES } from '~/data/games';

</script>

<style scoped>
.cont{
    display: flex;
    width: 100%;
    flex-direction: column;
}

.games{
    width: 100%;
    display: flex;
    flex-direction: column;
}

</style>