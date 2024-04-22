#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	prev_slow->next = NULL;

	reverse_list(&second_half);

	return (compare_lists(*head, second_half));
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the first list
 * @list2: pointer to the second list
 * Return: 0 if the lists are not equal, 1 if they are equal
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}

