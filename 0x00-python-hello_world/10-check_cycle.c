#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * @list: type listint_t
 * Return: always int
 * case: 1 true, 0 false
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;

	while (turtle != NULL && hare != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
