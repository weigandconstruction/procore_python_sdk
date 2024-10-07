# UpdateSegmentOrderBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_order** | [**List[UpdateSegmentOrderBodyUpdatedOrderInner]**](UpdateSegmentOrderBodyUpdatedOrderInner.md) | New position for each segment in the pattern | 

## Example

```python
from procore_sdk.models.update_segment_order_body import UpdateSegmentOrderBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSegmentOrderBody from a JSON string
update_segment_order_body_instance = UpdateSegmentOrderBody.from_json(json)
# print the JSON string representation of the object
print(UpdateSegmentOrderBody.to_json())

# convert the object into a dict
update_segment_order_body_dict = update_segment_order_body_instance.to_dict()
# create an instance of UpdateSegmentOrderBody from a dict
update_segment_order_body_from_dict = UpdateSegmentOrderBody.from_dict(update_segment_order_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


