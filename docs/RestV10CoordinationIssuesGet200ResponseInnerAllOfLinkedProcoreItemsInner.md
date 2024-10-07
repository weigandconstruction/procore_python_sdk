# RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**coordination_issue_id** | **int** | Id of the associated Coordination Issue | [optional] 
**item_id** | **int** | Id of the associated Procore item | [optional] 
**item_type** | **str** | Type of the associated Procore item | [optional] 
**item_url** | **str** | Deep-link URL to the associated Procore item | [optional] 
**item_data** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData**](RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner import RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_dict = rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInner.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


