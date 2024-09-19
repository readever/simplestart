<template>
    <!--<el-tag>{{item.value}}</el-tag>-->
    <v-row>
    <v-rating
      v-model="rating" density="compact" color="orange" half-increments></v-rating>
    <v-chip variant="text">{{item.value}}</v-chip>
        </v-row>
</template>

<script>

module.exports = {
    props:["item"],
    
    data () {
        return {
            rating: 3
        }
    },
    methods: {
        //todo
    },
    mounted: function () {
        this.rating = this.item.value/20
    },
}
</script>