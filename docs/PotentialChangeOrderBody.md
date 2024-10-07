# PotentialChangeOrderBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | [**List[PotentialChangeOrderBodyUpdatesInner]**](PotentialChangeOrderBodyUpdatesInner.md) |  | 

## Example

```python
from procore_sdk.models.potential_change_order_body import PotentialChangeOrderBody

# TODO update the JSON string below
json = "{}"
# create an instance of PotentialChangeOrderBody from a JSON string
potential_change_order_body_instance = PotentialChangeOrderBody.from_json(json)
# print the JSON string representation of the object
print(PotentialChangeOrderBody.to_json())

# convert the object into a dict
potential_change_order_body_dict = potential_change_order_body_instance.to_dict()
# create an instance of PotentialChangeOrderBody from a dict
potential_change_order_body_from_dict = PotentialChangeOrderBody.from_dict(potential_change_order_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


