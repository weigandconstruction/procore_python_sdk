# RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner

CoordinationIssue linked Observation Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**number** | **str** | Observation Item number | [optional] 
**personal** | **bool** | Observation Item privacy status | [optional] 
**title** | **str** | Formatted Observation Item title | [optional] 
**url** | **str** | Deep-link URL to Observation Item | [optional] 
**created_by_id** | **int** | ID of user that created the Observation Item | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_linked_observation_items_inner import RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_linked_observation_items_inner_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_linked_observation_items_inner_dict = rest_v10_coordination_issues_get200_response_inner_all_of_linked_observation_items_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_linked_observation_items_inner_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedObservationItemsInner.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_linked_observation_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


