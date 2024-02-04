def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
