<template>
  <div class="container mx-auto px-2 sm:px-10 py-2 lg:md:max-w-4xl">
    <FormComponent @submit="createUser">
      <template #form-inputs>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div class="mb-4 sm:mb-2 md:mb-0">
            <FormInput
              id="email"
              label="Email"
              :required="true"
              :type="'email'"
              :placeholder="'Email'"
              v-model="user.email"
              class="w-full p-2 border border-gray-300 rounded-md"
            >
              <template #icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="1em"
                  viewBox="0 0 512 512"
                >
                  <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                  <path
                    d="M64 112c-8.8 0-16 7.2-16 16v22.1L220.5 291.7c20.7 17 50.4 17 71.1 0L464 150.1V128c0-8.8-7.2-16-16-16H64zM48 212.2V384c0 8.8 7.2 16 16 16H448c8.8 0 16-7.2 16-16V212.2L322 328.8c-38.4 31.5-93.7 31.5-132 0L48 212.2zM0 128C0 92.7 28.7 64 64 64H448c35.3 0 64 28.7 64 64V384c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V128z"
                  />
                </svg>
              </template>
            </FormInput>
          </div>

          <div class="mb-4 sm:mb-2 md:mb-0">
            <FormInput
              id="first_name"
              label="First Name"
              :required="true"
              v-model="user.first_name"
              :placeholder="'First Name'"
              class="w-full p-2 border border-gray-300 rounded-md"
            >
              <template #icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="1em"
                  viewBox="0 0 512 512"
                >
                  <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                  <path
                    d="M362.7 19.3L314.3 67.7 444.3 197.7l48.4-48.4c25-25 25-65.5 0-90.5L453.3 19.3c-25-25-65.5-25-90.5 0zm-71 71L58.6 323.5c-10.4 10.4-18 23.3-22.2 37.4L1 481.2C-1.5 489.7 .8 498.8 7 505s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L421.7 220.3 291.7 90.3z"
                  />
                </svg>
              </template>
            </FormInput>
            <span
              v-if="showInvalidInputMessage(user.first_name, 'first_name')"
              class="text-red-500"
              >Invalid input: Only letters are allowed.</span
            >
          </div>
          <div class="mb-4 sm:mb-2 md:mb-0">
            <FormInput
              id="last_name"
              label="Last Name"
              :required="true"
              :placeholder="'First Name'"
              v-model="user.last_name"
              class="w-full p-2 border border-gray-300 rounded-md"
            >
              <template #icon>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="1em"
                  viewBox="0 0 512 512"
                >
                  <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                  <path
                    d="M362.7 19.3L314.3 67.7 444.3 197.7l48.4-48.4c25-25 25-65.5 0-90.5L453.3 19.3c-25-25-65.5-25-90.5 0zm-71 71L58.6 323.5c-10.4 10.4-18 23.3-22.2 37.4L1 481.2C-1.5 489.7 .8 498.8 7 505s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L421.7 220.3 291.7 90.3z"
                  />
                </svg> </template
            ></FormInput>
            <span
              v-if="showInvalidInputMessage(user.last_name, 'last_name')"
              class="text-red-500"
              >Invalid input: Only letters are allowed.</span
            >
          </div>

          <div class="mb-4 sm:mb-2 md:mb-0">
            <Dropdown
              :user="user"
              :selectedItem="selectedAvatar"
              :isOpen="isOpen"
              :options="avatarOptions"
              :toggleDropdown="toggleDropdown"
              :selectItem="selectAvatar"
            >
              <template #placeholder>
                <span class="text-gray-500">Select an Avatar</span>
              </template>
            </Dropdown>
          </div>

          <div class="mb-4 sm:mb-2 md:mb-0">
            <button
              type="submit"
              class="bg-blue-500 text-white font-bold py-2 px-4 rounded-md w-full h-[3rem] md:h-auto disabled:opacity-50"
              :disabled="isButtonDisabled"
            >
              Create User
            </button>
          </div>
        </div>
      </template>
    </FormComponent>
    <AlertMessage :message="serverResponseMessage" />
    <List
      :items="users"
      @item-clicked="navigateToUserDetail"
      :displayLabels="displayLabels"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, reactive, watch } from "vue";
import axios from "axios";
import FormComponent from "@/components/FormComponent.vue";
import FormInput from "@/components/FormInput.vue";
import List from "@/components/ListComponent.vue";
import Dropdown from "@/components/DropDownComponent.vue";
import AlertMessage from "@/components/widgets/AlertComponent.vue";
import router from "@/router";
import {
  hasInvalidChars as hasInvalidCharsValidation,
  hasEmptyFields as hasEmptyFieldsValidation,
  isButtonDisabled as isButtonDisabledValidation,
  showInvalidInputMessage as showInvalidInputMessageValidation,
  serverResponseMessage as serverResponseMessageValidation,
} from "@/utils/validationUtils";
import { createFilteredUsers } from "@/utils/filtersUtils";

import { createComputedProperty } from "@/utils/displayLabelsUtils";

interface User {
  email: string;
  first_name: string;
  last_name: string;
  avatar: string;
}


export default defineComponent({
  components: {
    FormComponent,
    FormInput,
    List,
    Dropdown,
    AlertMessage
  },
  setup() {
    const user = ref({
      email: "",
      first_name: "",
      last_name: "",
      avatar: "",
    });

    const keyValuePairs = {
      first_name: "First Name",
      last_name: "Last Name",
      email: "Email",
    };

    const users = ref([]);
    const isSubmitting = ref(false);
    const avatarOptions = ref([]);
    const isOpen = ref(false);
    const selectedAvatar = ref(null);
    const showInvalidInputError = ref(false);
    const errors = reactive({});
    errors["create_user"] = ref(null);
    
    
    const createUser = async (): Promise<void> => {
      if (isSubmitting.value || showInvalidInputError.value) {
        return;
      }
      isSubmitting.value = true;
      try {
        const response = await axios.post(
          "http://localhost:8000/api/users/create/",
          user.value
        );
        /* 
           In order to further avoid multiple api calls, 
           I am getting the response data from create user endpoint 
           and then adding it to to the users state to update 
           the list with latest created user
        */
        users.value.unshift(response.data);
        user.value = {
          email: "",
          first_name: "",
          last_name: "",
          avatar: "",
        };
        showInvalidInputError.value = false;
        errors["create_user"] = null;
      } catch (err) {
        errors["create_user"] = err;
      } finally {
        isSubmitting.value = false;
      }
    };

    const hasInvalidChars = hasInvalidCharsValidation;
    const hasEmptyFields = hasEmptyFieldsValidation(user);
    const isButtonDisabled = isButtonDisabledValidation(
      isSubmitting,
      errors,
      hasEmptyFields
    );
    const showInvalidInputMessage = showInvalidInputMessageValidation(
      hasInvalidChars,
      errors
    );
    const serverResponseMessage = serverResponseMessageValidation(errors);

    // I setup it up specifically to allow the user to submit again after error is displayed for sometime
    watch(serverResponseMessage, (newResponseMessage) => {
        if (newResponseMessage) {
          
          user.value = {
            email: "",
            first_name: "",
            last_name: "",
            avatar: "",
          };
        
          setTimeout(() => {
            errors["create_user"] = null;
          }, 2000); 
          
        }
      });


    const toggleDropdown = (event: any) => {
      event.preventDefault();
      isOpen.value = !isOpen.value;
    };

    const closeDropdown = () => {
      isOpen.value = !isOpen.value;
    };

    const selectAvatar = (avatar: any) => {
      selectedAvatar.value = avatar;
      user.value.avatar = selectedAvatar.value;
      closeDropdown();
    };

    onMounted(async () => {
      try {
        /* The main purpose is to reduce number of api calls, 
           so it will be initially called onMounted */
        const usersResponse = await axios.get(
          "http://localhost:8000/api/users/"
        );
        users.value = usersResponse.data;

        // I used the same api to call for random avatars
        const avatarsResponse = await axios.get(
          "https://reqres.in/api/users?page=2"
        );
        avatarOptions.value = avatarsResponse.data.data.map(
          (user) => user.avatar
        );
      } catch (error) {
        console.error("Error fetching users or avatars:", error);
      }
    });

    const displayLabels = createComputedProperty(keyValuePairs);
    const navigateToUserDetail = (item) => {
      router.push({ name: "UserDetail", params: { id: item.id } });
    };

    return {
      user,
      keyValuePairs,
      users: createFilteredUsers(users),
      createUser,
      avatarOptions,
      isOpen,
      selectedAvatar,
      toggleDropdown,
      selectAvatar,
      displayLabels,
      hasInvalidChars,
      showInvalidInputMessage,
      showInvalidInputError,
      isButtonDisabled,
      serverResponseMessage,
      navigateToUserDetail
    };
  },
});
</script>
