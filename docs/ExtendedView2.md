# ExtendedView2

Project Person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**NormalContact**](NormalContact.md) |  | [optional] 
**employee_id** | **str** | Employee ID for the Project Person | [optional] 
**first_name** | **str** | Project Person first name | [optional] 
**id** | **int** | Unique identifier for the Project Person. | [optional] 
**is_employee** | **bool** | Employee status for the Project Person | [optional] 
**last_name** | **str** | Project Person last name | [optional] 
**user_id** | **int** | User ID if this Project Person represents a User. NULL for a Reference User. | [optional] 
**user_uuid** | **int** | The user UUID for if this Company Person represents a user. This value is set to NULL for a Reference User. | [optional] 
**work_classification_id** | **int** | Work Classification ID for the Project Person | [optional] 
**origin_id** | **int** | The ID of the External Data associated with the Project Person | [optional] 
**work_classification** | [**ExtendedViewWorkClassification**](ExtendedViewWorkClassification.md) |  | [optional] 
**vendor** | [**Compact**](Compact.md) |  | [optional] 

## Example

```python
from procore_sdk.models.extended_view2 import ExtendedView2

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedView2 from a JSON string
extended_view2_instance = ExtendedView2.from_json(json)
# print the JSON string representation of the object
print(ExtendedView2.to_json())

# convert the object into a dict
extended_view2_dict = extended_view2_instance.to_dict()
# create an instance of ExtendedView2 from a dict
extended_view2_from_dict = ExtendedView2.from_dict(extended_view2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


