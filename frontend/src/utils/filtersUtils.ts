import { computed, Ref } from "vue";

interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  avatar: string;
}

const createFilteredUsers = (users: Ref<User[]>) => {
  return computed(() => {
    return users.value.map((user) => {
      const { avatar, ...rest } = user;
      return rest;
    });
  });
};

export { createFilteredUsers };
