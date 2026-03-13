<template>
    <section v-if="character" class="character">
        <img class="icon" :src="character.icon || '/placeholder-avatar.png'" alt="Иконка персонажа" />

        <div class="character-wrapper">
            <p><strong>Имя персонажа:</strong> {{ character.name }}</p>
            <p><strong>Описание:</strong> {{ character.description || 'Нет описания' }}</p>
            <p><strong>Автор:</strong> {{ character.author?.userName || 'Неизвестен' }}</p>

            <p><strong>Характеристики</strong></p>
            <ul class="stats-list" v-if="hasStats">
                <li class="stat" v-for="(value, key) in character.stats" :key="key">
                    {{ capitalize(key) }}: {{ value }}
                </li>
            </ul>
            <p v-else class="no-data">Характеристики не указаны</p>

            <p><strong>Квесты/игры</strong></p>
            <ul class="games-list" v-if="character.games?.length">
                <li class="game" v-for="game in character.games" :key="game.gameId">
                    {{ game.gameName }}
                </li>
            </ul>
            <p v-else class="no-data">Нет связанных квестов или игр</p>

            <!-- Сообщение после удаления -->
            <p v-if="deleteMessage" :class="{ success: deleteSuccess, error: !deleteSuccess }">
                {{ deleteMessage }}
            </p>

            <menu class="menu">
                <button class="btn-delete" @click="handleDelete">Удалить</button>
                <NuxtLink class="btn-edit" :to="`./charForm/${character.id}`">
                    Редактировать
                </NuxtLink>
            </menu>
        </div>
    </section>

    <div v-else-if="error" class="error">
        Персонаж не найден или произошла ошибка
    </div>

    <div v-else class="loading">
        Загрузка персонажа...
    </div>
</template>

<script setup lang="ts">
import type { Character } from '~/data/characters'
import { getCharById, deleteChar } from '~/api/charactersAPI'
import { useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const characterId = computed(() => route.params.id as string)

// Загрузка персонажа
const { data: character, error, pending } = await useAsyncData(
    `character-${characterId.value}`,
    () => getCharById(characterId.value)
)

const hasStats = computed(() =>
    character.value?.stats && Object.keys(character.value.stats).length > 0
)

const capitalize = (str: string): string =>
    str.charAt(0).toUpperCase() + str.slice(1).toLowerCase()

// Состояние для удаления
const deleteMessage = ref('')
const deleteSuccess = ref(false)

async function handleDelete() {
    if (!confirm('Вы уверены, что хотите удалить этого персонажа? Это действие нельзя отменить.')) {
        return
    }

    try {
        await deleteChar(characterId.value)
        deleteSuccess.value = true
        deleteMessage.value = 'Персонаж успешно удалён!'

        // Редирект на профиль через 1 секунду
        setTimeout(() => {
            router.push('/profile/0')
        }, 1000)
    } catch (err) {
        deleteSuccess.value = false
        deleteMessage.value = 'Ошибка при удалении персонажа. Попробуйте позже.'
        console.error(err)
    }
}

watch(characterId, () => refreshNuxtData(`character-${characterId.value}`))
</script>

<style scoped>
.character {
    display: flex;
    align-items: flex-start;
    gap: 75px;
    padding: 20px;
    margin: 40px 0;
    border: 1px solid #ddd;
    border-radius: 12px;
    background: #fcfcfc;
}

.icon {
    width: 200px;
    height: 200px;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid #000;
    background: #eee;
}

.character-wrapper p {
    margin: 12px 0;
    max-width: 770px;
}

ul {
    list-style: none;
    padding-left: 0;
    margin: 12px 0;
}

.stat,
.game {
    padding: 6px 0;
    border-bottom: 1px dashed #ccc;
}

.no-data {
    color: #888;
    font-style: italic;
}

.loading {
    text-align: center;
    padding: 40px;
    color: #666;
}

.error {
    text-align: center;
    padding: 40px;
    color: #d00;
}

.menu {
    display: flex;
    justify-content: space-between;
    margin-top: 24px;
    gap: 1rem;
}

.btn-delete,
.btn-edit {
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s ease;
}

.btn-delete {
    background: #ff4444;
    color: white;
}

.btn-delete:hover {
    background: #cc0000;
}

.btn-edit {
    background: #0066ff;
    color: white;
    text-decoration: none;
}

.btn-edit:hover {
    background: #0052cc;
}

.success {
    color: #00aa00;
    font-weight: 600;
    text-align: center;
    margin-top: 1rem;
}

.error {
    color: #ff4444;
    font-weight: 600;
    text-align: center;
    margin-top: 1rem;
}
</style>