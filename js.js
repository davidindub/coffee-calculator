function Calculate(e) {
	var t,
		a = $('#hd').val();
	t = e ? 1 * e : 1 * a;
	var o = parseFloat($('#wsel').val()),
		l = parseFloat($('#gsel').val()),
		r = parseFloat($('#brsel').val()),
		n = parseInt($('#wcrat').val()),
		u = parseFloat($('#valw').val()),
		c = parseFloat($('#valgr').val()),
		i = parseFloat($('#valbr').val());
	switch (t) {
		case 1:
			var v = (o * u / (l * n)).toFixed(2);
			$('#valgr').val(v);
			var s = ((o * u - 1.995 * l * v) / r).toFixed(2);
			$('#valbr').val(s), $('#hd').val(1);
			break;
		case 2:
			var d = (n * c * l / o).toFixed(2);
			$('#valw').val(d);
			var h = ((o * d - 1.995 * l * c) / r).toFixed(2);
			$('#valbr').val(h), $('#hd').val(2);
			break;
		case 3:
			var v = (r * i / (n - 1.995) / l).toFixed(2);
			$('#valgr').val(v);
			var p = (n * v * l / o).toFixed(2);
			$('#valw').val(p), $('#hd').val(3);
	}
}
$(function() {
	var e = $('#wcrat'),
		t = $('#brsel'),
		a = $('#jqsld').insertAfter(t).slider({
			value: e[0].selectedIndex + 1,
			slide: function(t, a) {
				(e[0].selectedIndex = a.value - 1), Calculate();
			}
		});
	$('#wcrat').on('change', function() {
		a.slider('value', this.selectedIndex + 1);
	});
}),
	!(function(e) {
		function t(e, t) {
			if (!(e.originalEvent.touches.length > 1)) {
				e.preventDefault();
				var a = e.originalEvent.changedTouches[0],
					o = document.createEvent('MouseEvents');
				o.initMouseEvent(
					t,
					!0,
					!0,
					window,
					1,
					a.screenX,
					a.screenY,
					a.clientX,
					a.clientY,
					!1,
					!1,
					!1,
					!1,
					0,
					null
				),
					e.target.dispatchEvent(o);
			}
		}
		if (((e.support.touch = 'ontouchend' in document), e.support.touch)) {
			var a,
				o = e.ui.mouse.prototype,
				l = o._mouseInit,
				r = o._mouseDestroy;
			(o._touchStart = function(e) {
				var o = this;
				!a &&
					o._mouseCapture(e.originalEvent.changedTouches[0]) &&
					((a = !0), (o._touchMoved = !1), t(e, 'mouseover'), t(e, 'mousemove'), t(e, 'mousedown'));
			}),
				(o._touchMove = function(e) {
					a && ((this._touchMoved = !0), t(e, 'mousemove'));
				}),
				(o._touchEnd = function(e) {
					a && (t(e, 'mouseup'), t(e, 'mouseout'), this._touchMoved || t(e, 'click'), (a = !1));
				}),
				(o._mouseInit = function() {
					var t = this;
					t.element.bind({
						touchstart: e.proxy(t, '_touchStart'),
						touchmove: e.proxy(t, '_touchMove'),
						touchend: e.proxy(t, '_touchEnd')
					}),
						l.call(t);
				}),
				(o._mouseDestroy = function() {
					var t = this;
					t.element.unbind({
						touchstart: e.proxy(t, '_touchStart'),
						touchmove: e.proxy(t, '_touchMove'),
						touchend: e.proxy(t, '_touchEnd')
					}),
						r.call(t);
				});
		}
	})(jQuery),
	$(document).ready(function() {
		var e = { orientation: 'horizontal', animate: !0, range: 'min', min: 1, max: 7 };
		$('#jqsld').slider(e),
			$('#jqsld').each(function() {
				for (var e = $(this).data().uiSlider.options, t = e.max - e.min, a = 0; t >= a; a++) {
					var o = $('<label>Strong</label>').css('left', a / t * 100 + '%'),
						l = $('<label>Normal</label>').css('left', a / t * 100 + '%'),
						r = $('<label>Weak</label>').css('left', a / t * 100 + '%');
					0 == a && $('#jqsld').append(o), 3 == a && $('#jqsld').append(l), 6 == a && $('#jqsld').append(r);
				}
			}),
			Calculate();
	});
