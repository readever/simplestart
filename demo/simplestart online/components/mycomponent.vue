<template>
  <div class="my-component">
    <h1>{{title}}: {{ data.language }}</h1>
    <el-button @click="testme">handle on server</el-button>
  </div>
</template>

<script>
module.exports = {
    name: 'MyComponent',

    data() {
        return {
            title:"computer",
        }
    },

    methods: {
        testme(){
            this.streamsync.forwardData(this, eventname="ontest", "12345")
        }
    }
}
</script>

<style>
.my-component {
    width:50%;
    background-color: #f0f0f0;
    padding: 20px;
    margin:10px 0;
}
</style>
