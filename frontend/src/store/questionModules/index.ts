import axios, { AxiosResponse } from 'axios'

interface Answer {
    id: number
    name: string;
    create_at: string;
}

interface AnswerText {
    id: number
    name: string;
    create_at: string;
}

interface Question {
    id: number;
    quest: string;
    create_at: any;
    answer: Answer[];
    answer_text: AnswerText[];
}

interface PointState {
    point: number;
}

interface QuestionState {
    readonly question: Question[];
    readonly data: Question
    readonly point: PointState;
}

const state: QuestionState = {
    question: [],
    data: {
        id: 0,
        quest: '',
        create_at: '',
        answer: [],
        answer_text: [],
    },
    point: {
        point: 0
    }
    
}

interface AnswerState {
    pk: number;
    answer: string;
}

interface UserState {
    first_name: string;
    last_name: string;
}

const actions = {
    async fetchQuestion({commit}: any) {
        const response = await axios.get('http://localhost:8000/api/v1/question/').then((res: AxiosResponse) => {
            commit('FETCH_Q', res.data)
        })
        return response
    },
    async detailQuestion({commit}: any, newValue: number) {
        const response = await axios.get(`http://localhost:8000/api/v1/question/${newValue}/`)
        return response
    },
    async answersQuestion({commit}: any, newValue: AnswerState) {
        const response = await axios.put(`http://localhost:8000/api/v1/question/question/answer/${newValue.pk}/`, {
            'answers': newValue.answer
        }, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
        })
        return response
    },
    async register({commit}: any, newValue: UserState) {
        const response = await axios.post(`http://localhost:8000/api/v1/user/`, newValue)
        return response
    },
}
const mutations = {
    FETCH_Q: (fetch: QuestionState | any, data: any) => fetch.question = data,
    DETAIL_FETCH_Q: (fetch: QuestionState | any, data: any) => fetch.data = data,
    POINT_QUESTION: (point: QuestionState, data: any) => point.point.point = data
}
const getters = {
    question: (fetch: QuestionState) => fetch.question,
    detail: (fetch: QuestionState) => fetch.data,
    getPoint: (point: QuestionState) => point.point
}

export default {
    state,
    actions,
    mutations,
    getters
}