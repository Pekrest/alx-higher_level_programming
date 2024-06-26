#include "lists.h"
#include <stdbool.h>

int is_palindrome(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_list - reverse the linked listi
 *
 * @head: head of the list
 *
 * Return: resturns the prev list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *current = head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a singly linked
 * list is a palindrome
 *
 * @head: head of the list
 * Return: returns 0 or 1
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *middle = NULL;

	if (*head == NULL)
	{
		return (1);
	}
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	slow = reverse_list(slow);
	fast = *head;
	while (slow != NULL)
	{
		if (fast->n != slow->n)
		{
			return (0);
		}
		fast = fast->next;
		slow = slow->next;
	}
	slow = reverse_list(slow);
	if (middle != NULL)
	{
		prev_slow->next = middle;
		middle->next = slow;
	}
	else
		prev_slow->next = slow;

	return (1);
}
