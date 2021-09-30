#include "lists.h"

/**
 * check - recursive function to check a listint_t for a palindrome
 * @head: head node of singly linked list
 * @temp: will point to last item of list
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int check(listint_t **head, listint_t *temp)
{
	if (!temp)
		return (1);
	if ((*head)->n == temp->n && check(head, temp->next))
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - calls check recursively for palindrome match
 * @head: head node of list
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (check(head, *head));
}
