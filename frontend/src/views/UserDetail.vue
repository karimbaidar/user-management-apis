<template>
  <div class="max-w-[2xl] mx-auto">
    <div v-if="isLoading" class="flex justify-center items-start min-h-screen">
      <div
        class="animate-spin w-10 h-10 border-t-4 border-blue-500 border-solid rounded-full"
      ></div>
    </div>
    <div v-if="!isLoading">
      <div class="flex justify-center mb-5">
        <button @click="goBack">Go Back</button>
      </div>
      <UserCard :user="user" :fields="fields" :avatar="avatarKey" />
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import UserCard from "@/components/UserCardComponent.vue";

export default {
  components: {
    UserCard,
  },
  setup() {
    const user = ref(null);
    const route = useRoute();
    const router = useRouter();
    const fields = [
      { key: "email", label: "Email" },
      { key: "first_name", label: "First Name" },
      { key: "last_name", label: "Last Name" },
    ];
    const avatarKey = "avatar";
    const isLoading = ref(true);

    const fetchUserDetails = () => {
      const userId = route.params.id;
      axios
        .get(`http://localhost:8000/api/users/${userId}/`)
        .then((response) => {
          user.value = response.data;
          isLoading.value = false;
        })
        .catch((error) => {
          console.error("Error fetching user details:", error);
          isLoading.value = false;
        });
    };

    onMounted(fetchUserDetails);

    const goBack = () => {
      router.back();
    };

    return {
      user,
      fields,
      avatarKey,
      router,
      isLoading,
      goBack
    };
  }
};
</script>
