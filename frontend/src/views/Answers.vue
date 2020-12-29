<template>
    <div>
        {{getPoint.point}}
        <div class="knd-newbie-card">
            <p>
                {{detail.quest}}
            </p>
            <div class="knd-newbie-group" v-if="detail.answer.length">
                <div v-for="answers in detail.answer" :key="answers.id">
                    <button class="knd-newbie-button" v-on:click="handleClickAnswer(answers.id, answers.name)">
                        {{answers.name}}
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { mapGetters } from 'vuex';
import { AxiosResponse } from 'axios'

@Component({
    computed: mapGetters(['detail','getPoint'])
})
export default class Answers extends Vue {
    $route: any;
    $vs : any;
    handleClickAnswer(choice: number, value: string) {
        const data = {
            pk: choice,
            answer: value
        }
        this.$store.dispatch("answersQuestion", data).then((res: AxiosResponse<any>) => {
            this.$store.commit("POINT_QUESTION", res.data.point)
            this.$vs.notification({
                color: 'success',
                position: 'top-right',
                text: res.data.message
            })
        }).catch((err) => {
            this.$store.commit("POINT_QUESTION", err.response.data.point)
            this.$vs.notification({
            color: 'danger',
            position: 'top-right',
            text: err.response.data.message
          })
        })
    }
    mounted() {
        this.$store.dispatch('detailQuestion', this.$route.params.id).then((res: AxiosResponse<any>) => {
            this.$store.commit("DETAIL_FETCH_Q", res.data)
        })
    }
}
</script>

<style lang="scss">
.knd-newbie-card {
    border-radius: 10px;
    background-color: #42b983;
    color: white;
    box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
    padding: 1rem;
    width: 80%;
    margin: auto;
}
.knd-newbie-group {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
    .knd-newbie-button {
        margin: 0.40rem;
        cursor: pointer;
        padding-left: 1rem;
        padding-right: 1rem;
        margin-right: 1rem;
        margin-left: 1rem;
        border: none;
        outline: none;
        border-radius: 10px;
        height: 40px;
        background-color: white;
        box-shadow: 0 -2px 5px -2px rgba(0,0,0,0.75);
    }
}
textarea {
    resize: none;
    width: 100%;
    border: none;
    outline: none;
    border-radius: 10px;
    padding: 0.30rem;
}

.knd-newbie-form {
    width: 98%;
}

#knd-newbie-ad {
    width: 130px;
    justify-content: center;
    display: flex;
    align-items: center;
    text-align: center;
    margin-left: 0;
}
</style>