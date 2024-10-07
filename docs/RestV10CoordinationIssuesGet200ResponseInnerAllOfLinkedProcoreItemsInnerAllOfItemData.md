# RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData

This field shows data specific to the associated item. If item type is RFI, it will contain attribute subject, number, and has_official_response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_official_response** | **bool** |  | [optional] 
**subject** | **str** |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_all_of_item_data import RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_all_of_item_data_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_all_of_item_data_dict = rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_all_of_item_data_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_all_of_item_data_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfLinkedProcoreItemsInnerAllOfItemData.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_linked_procore_items_inner_all_of_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


