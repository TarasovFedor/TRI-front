<template>
    <div class="add-character-page">
        <h1>Добавить нового персонажа</h1>

        <form @submit.prevent="submitForm" class="add-char-form">
            <label class="form-label">
                <span>Имя персонажа</span>
                <input v-model="form.name" type="text" minlength="3" maxlength="15" required
                    placeholder="От 3 до 15 символов" />
            </label>

            <label class="form-label">
                <span>Описание</span>
                <textarea v-model="form.description" minlength="3" rows="5"
                    placeholder="Краткое описание персонажа"></textarea>
            </label>

            <div class="stats-section">
                <div class="section-header">
                    <span>Характеристики</span>
                    <button type="button" @click="addStat" class="btn-add-stat">
                        + Добавить характеристику
                    </button>
                </div>

                <div v-for="(stat, index) in form.stats" :key="index" class="stat-row">
                    <input v-model="stat.key" type="text" placeholder="Название (сила, ловкость...)" required />
                    <input v-model.number="stat.value" type="number" placeholder="Значение" min="0" required />
                    <button type="button" @click="removeStat(index)" class="btn-remove">
                        ✕
                    </button>
                </div>

                <p v-if="form.stats.length === 0" class="no-stats">
                    Пока нет характеристик
                </p>
            </div>

            <div class="form-actions">
                <button type="submit" class="btn-submit" :disabled="isSubmitting">
                    {{ isSubmitting ? 'Добавляем...' : 'Добавить персонажа' }}
                </button>
            </div>

            <p v-if="message" :class="{ success: isSuccess, error: !isSuccess }">
                {{ message }}
            </p>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { postChar } from '~/api/charactersAPI'
import type { Character } from '~/data/characters'

const router = useRouter()

const form = reactive({
    name: '',
    description: '',
    icon: '',
    stats: [] as Array<{ key: string; value: number }>
})

const isSubmitting = ref(false)
const message = ref('')
const isSuccess = ref(false)

function addStat() {
    form.stats.push({ key: '', value: 0 })
}

function removeStat(index: number) {
    form.stats.splice(index, 1)
}

async function submitForm() {
    if (form.name.trim().length < 3) return

    isSubmitting.value = true
    message.value = ''
    isSuccess.value = false

    try {
        const statsObject = form.stats.reduce((acc, stat) => {
            if (stat.key.trim()) {
                acc[stat.key.trim()] = stat.value
            }
            return acc
        }, {} as Record<string, number>)

        const newCharacter: Character = {
            name: form.name.trim(),
            icon: '',
            description: form.description.trim(),
            stats: statsObject,
            authorId: 0,
            gameId: 0
        }

        await postChar(newCharacter)

        isSuccess.value = true
        message.value = 'Персонаж успешно добавлен!'

        form.name = ''
        form.description = ''
        form.icon = ''
        form.stats = []

        setTimeout(() => {
            router.push('/profile/0')
        }, 2000)
    } catch (error) {
        isSuccess.value = false
        message.value = 'Ошибка при добавлении персонажа. Попробуйте позже.'
        console.error(error)
    } finally {
        isSubmitting.value = false
    }
}
</script>

<style scoped>
.add-character-page {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 1rem;
}

h1 {
    margin-bottom: 2rem;
    text-align: center;
}

.add-char-form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    background: #f9f9f9;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.form-label {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    font-weight: 600;
}

.form-label span {
    color: #333;
}

input,
textarea {
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1rem;
}

input:focus,
textarea:focus {
    outline: none;
    border-color: #0066ff;
    box-shadow: 0 0 0 3px rgba(0, 102, 255, 0.2);
}

.stats-section {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 600;
}

.btn-add-stat {
    background: #0066ff;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
}

.btn-add-stat:hover {
    background: #0052cc;
}

.stat-row {
    display: grid;
    grid-template-columns: 1fr 1fr auto;
    gap: 0.75rem;
    align-items: center;
}

.btn-remove {
    background: #ff4444;
    color: white;
    border: none;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1.2rem;
}

.no-stats {
    color: #888;
    font-style: italic;
    margin: 0;
}

.form-actions {
    text-align: center;
}

.btn-submit {
    background: #00aa00;
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 8px;
    font-size: 1.1rem;
    cursor: pointer;
}

.btn-submit:hover:not(:disabled) {
    background: #008800;
}

.btn-submit:disabled {
    background: #aaa;
    cursor: not-allowed;
}

.success {
    color: #00aa00;
    font-weight: 600;
    text-align: center;
}

.error {
    color: #ff4444;
    font-weight: 600;
    text-align: center;
}
</style>