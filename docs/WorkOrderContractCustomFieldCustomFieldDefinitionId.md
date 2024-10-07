# WorkOrderContractCustomFieldCustomFieldDefinitionId

Value of the custom field. The data type of the value passed in corresponds with the data_type of the Custom Field Definition. For a lov_entry data_type the value passed in should be the ID of one of the Custom Field Definition's LOV Entries. For a lov_entries data_type the value passed in should be an array of IDs of the Custom Field Definition's LOV Entries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderContractCustomFieldCustomFieldDefinitionId from a JSON string
work_order_contract_custom_field_custom_field_definition_id_instance = WorkOrderContractCustomFieldCustomFieldDefinitionId.from_json(json)
# print the JSON string representation of the object
print(WorkOrderContractCustomFieldCustomFieldDefinitionId.to_json())

# convert the object into a dict
work_order_contract_custom_field_custom_field_definition_id_dict = work_order_contract_custom_field_custom_field_definition_id_instance.to_dict()
# create an instance of WorkOrderContractCustomFieldCustomFieldDefinitionId from a dict
work_order_contract_custom_field_custom_field_definition_id_from_dict = WorkOrderContractCustomFieldCustomFieldDefinitionId.from_dict(work_order_contract_custom_field_custom_field_definition_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


