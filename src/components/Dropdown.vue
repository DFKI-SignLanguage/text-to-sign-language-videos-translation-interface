<template>
    <div class="menu-item">
        <a href="#">
            {{ title }}
        </a>
        <svg viewBox="0 0 1030 638" width="10">
           <path d="M1017 68L541 626q-11 12-26 12t-26-12L13
           68Q-3 49 6 24.5T39 0h952q24 0 33 24.5t-7 43.5z" fill="#FFF"></path>
        </svg>  
        <div class="sub-menu">
            <div v-for="(item, i) in items" :key="i" class="menu-item">
                <a href="item.link">{{ item.title }}</a>
            </div>
        </div> 
    </div>

</template>

<script>
export default {
    name: 'dropdown',
    props: ['title','items']
}
</script>

<style>
nav .menu-iem svg {
    width: 10px;
    margin-left: 10px;
}
</style>