#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct list_int - a singly linked list
 * @i: integer
 * @next_node: points to the next node
 *
 * Description: A singly linked list node structure
 * for Holberton project
 */
typedef struct list_int
{
	int i;
	struct list_int *next_node;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
