
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 4
        # example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "age": 33,
                "Lucky Numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "age": 35,
                "Lucky Numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "age": 5,
                "Lucky Numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            member["id"] = self._generateId()  # Assign a unique ID
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for item in self._members:
            if item["id"] == id:
                self._members.remove(item)
                return True
        return False

    def get_member(self, id):
        # fill this method and update the return
        for item in self._members:
            if item["id"] == id:
                return item
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
